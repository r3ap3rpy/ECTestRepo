from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

private_key = dsa.generate_private_key(
    key_size = 1024,
    backend=default_backend()
)

data = b"Cryptography is a very fun subject and worth to know and understand!"

signature = private_key.sign(data,hashes.SHA256())

public_key = private_key.public_key()

public_key.verify(
    signature,
    data,
    hashes.SHA256()
)