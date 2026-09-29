from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import base64


NAME = "Ed25519"
CATEGORY = "Modern Cryptography"
OPERATIONS = ["keygen", "sign", "verify"]


def keygen():
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    private_bytes = private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption()
    )

    public_bytes = public_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return {
        "private_key": private_bytes.decode(),
        "public_key": public_bytes.decode()
    }


def sign(text, private_key):
    private = serialization.load_pem_private_key(
        private_key.encode(),
        password=None
    )

    signature = private.sign(text.encode())

    return base64.b64encode(signature).decode()


def verify(text, signature, public_key):
    public = serialization.load_pem_public_key(
        public_key.encode()
    )

    try:
        public.verify(
            base64.b64decode(signature),
            text.encode()
        )

        return True

    except Exception:
        return False
