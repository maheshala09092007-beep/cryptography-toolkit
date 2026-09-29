from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
import base64


NAME = "Diffie-Hellman"
CATEGORY = "Modern Cryptography"
OPERATIONS = ["keygen", "exchange"]


def keygen():
    parameters = dh.generate_parameters(
        generator=2,
        key_size=2048
    )

    private_key = parameters.generate_private_key()
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

    parameters_bytes = parameters.parameter_bytes(
        serialization.Encoding.PEM,
        serialization.ParameterFormat.PKCS3
    )

    return {
        "parameters": parameters_bytes.decode(),
        "private_key": private_bytes.decode(),
        "public_key": public_bytes.decode()
    }


def exchange(private_key, peer_public_key):
    parameters = None

    private = serialization.load_pem_private_key(
        private_key.encode(),
        password=None
    )

    public = serialization.load_pem_public_key(
        peer_public_key.encode()
    )

    shared_secret = private.exchange(public)

    return base64.b64encode(shared_secret).decode()
