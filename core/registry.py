import importlib
import pkgutil


CATEGORIES = {
    "encoding": "Encoding",
    "classical": "Classical Cryptography",
    "modern": "Modern Cryptography",
    "hashing": "Hashing",
}


def discover_algorithms():
    algorithms = {}

    for package_name, category_name in CATEGORIES.items():

        package = importlib.import_module(
            f"algorithms.{package_name}"
        )

        algorithms[category_name] = []

        for module_info in pkgutil.iter_modules(package.__path__):

            if module_info.name.startswith("_"):
                continue

            module = importlib.import_module(
                f"algorithms.{package_name}.{module_info.name}"
            )

            if hasattr(module, "NAME"):
                algorithms[category_name].append(module)

        algorithms[category_name].sort(
            key=lambda module: module.NAME.lower()
        )

    return algorithms
