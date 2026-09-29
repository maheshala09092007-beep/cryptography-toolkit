from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64


NAME = "RSA"
CATEGORY = "Modern Cryptography"
OPERATIONS = ["keygen", "encrypt", "decrypt"]


def keygen():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=__import__(
            "cryptography.hazmat.primitives.serialization",
            fromlist=["Encoding"]
        ).Encoding.PEM,
        format=__import__(
            "cryptography.hazmat.primitives.serialization",
            fromlist=["PrivateFormat"]
        ).PrivateFormat.PKCS8,
        encryption_algorithm=__import__(
            "cryptography.hazmat.primitives.serialization",
            fromlist=["NoEncryption"]
        ).NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=__import__(
            "cryptography.hazmat.primitives.serialization",
            fromlist=["Encoding"]
        ).Encoding.PEM,
        format=__import__(
            "cryptography.hazmat.primitives.serialization",
            fromlist=["PublicFormat"]
        ).PublicFormat.SubjectPublicKeyInfo
    )

    return {
        "private_key": private_pem.decode(),
        "public_key": public_pem.decode()
    }


def encrypt(text, public_key):
    from cryptography.hazmat.primitives import serialization

    key = serialization.load_pem_public_key(
        public_key.encode()
    )

    ciphertext = key.encrypt(
        text.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.b64encode(ciphertext).decode()


def decrypt(text, private_key):
    from cryptography.hazmat.primitives import serialization

    key = serialization.load_pem_private_key(
        private_key.encode(),
        password=None
    )

    ciphertext = base64.b64decode(text)

    plaintext = key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plaintext.decode()
