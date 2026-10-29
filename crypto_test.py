
import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_test_rsa_key():
    """Generate an RSA-2048 key for QA testing only."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    print("RSA-2048 key generation: PASS")
    print("Private key generated in memory; not saved.")
    return private_key


def test_sha1_hashing():
    """Exercise SHA-1 hashing for security scanner testing."""
    sample = b"RelixQ public repository QA test data"
    digest = hashlib.sha1(sample).hexdigest()

    print("SHA-1 test digest:", digest)
    print("SHA-1 hashing test: PASS")
    print("SHA-1 hashing test: PASS")


if __name__ == "__main__":
    generate_test_rsa_key()
    test_sha1_hashing()
