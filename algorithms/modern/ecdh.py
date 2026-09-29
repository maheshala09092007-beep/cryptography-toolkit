from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import base64


NAME = "ECDH"
CATEGORY = "Modern Cryptography"
OPERATIONS = ["keygen", "exchange"]


def keygen():
    private_key = ec.generate_private_key(ec.SECP256R1())
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


def exchange(private_key, peer_public_key):
    private = serialization.load_pem_private_key(
        private_key.encode(),
        password=None
    )

    public = serialization.load_pem_public_key(
        peer_public_key.encode()
    )

    shared_secret = private.exchange(
        ec.ECDH(),
        public
    )

    return base64.b64encode(shared_secret).decode()
