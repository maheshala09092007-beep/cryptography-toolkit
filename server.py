"""HTTP API for the Flutter app. Put this file in the repo root, next to main.py.

    pip install fastapi uvicorn
    uvicorn server:app --host 0.0.0.0 --port 8000

It reuses core/registry.py, so every algorithm module with NAME and
OPERATIONS shows up automatically. It assumes each operation is a function
with the same name (aes.py: encrypt(text, key), decrypt(text, key)) and that
a second parameter means the algorithm needs a key.
"""
import inspect

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from core.registry import discover_algorithms

app = FastAPI(title="CryptoToolkit API")
ALGOS = discover_algorithms()  # {"Encoding": [module, ...], ...}


def operation_fn(module, op):
    fn = getattr(module, op, None)
    return fn if callable(fn) else None


def needs_key(module):
    for op in module.OPERATIONS:
        fn = operation_fn(module, op)
        if fn:
            return len(inspect.signature(fn).parameters) > 1
    return False


@app.get("/algorithms")
def algorithms():
    return {
        category: [
            {"name": m.NAME, "operations": list(m.OPERATIONS), "needs_key": needs_key(m)}
            for m in modules
        ]
        for category, modules in ALGOS.items()
    }


class ExecuteRequest(BaseModel):
    category: str
    algorithm: str
    operation: str
    text: str
    parameters: dict = {}


@app.post("/execute")
def execute(req: ExecuteRequest):
    module = next((m for m in ALGOS.get(req.category, []) if m.NAME == req.algorithm), None)
    if module is None:
        raise HTTPException(404, "Unknown algorithm")
    if req.operation not in module.OPERATIONS:
        raise HTTPException(400, "Unsupported operation")
    fn = operation_fn(module, req.operation)
    if fn is None:
        raise HTTPException(500, f"{module.NAME} has no function named '{req.operation}'")
    try:
        args = [req.text]
        if len(inspect.signature(fn).parameters) > 1:
            args.append(req.parameters.get("key", ""))
        return {"result": str(fn(*args))}
    except Exception as exc:
        raise HTTPException(400, str(exc))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
