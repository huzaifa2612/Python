# Install required library (run once)
# !pip install cryptography numpy

import numpy as np
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import time

print("✅ Libraries imported successfully!")

import numpy as np
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import time

start = time.time()

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=16384
)

public_key = private_key.public_key()

elapsed = time.time() - start

pub_numbers = public_key.public_key().key_size if hasattr(public_key, 'public_key') else public_key.key_size

print(f"✅ Key pair generated in {elapsed:.2f} seconds")



print(f"\n📄 Key Details:")
print(f"   Key Size      : {private_key.key_size} bits")
print(f"   Public Exponent (e) : 65537")
print(f"   Public Key    : Shared with school 📩")
print(f"   Private Key   : Stored securely on your machine 🔒")

print(pub_numbers)


# Student G3 grades to be sent securely
raw_grades = ["27", "34", "18", "42", "9", "31", "25", "7", "38", "20", "45", "29", "33", "12", "40", "16", "28", "6", "36"]

print("School's Side: Encrypting student grades...")
print(f"   Original Grades : {raw_grades}")
print()

encrypted_grades = []

for i, grade in enumerate(raw_grades):
    token = public_key.encrypt(
        grade.encode(),   # Convert string to bytes
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask Generation Function
            algorithm=hashes.SHA256(),                   # Hash algorithm
            label=None
        )
    )

    encrypted_grades.append(token)

    print(f"   Grade '{grade}' -> Encrypted Token [{i+1}]: {token[:30].hex()}... ({len(token)} bytes)")

print()
print(f"   Sent to Researcher: {len(encrypted_grades)} encrypted tokens.")
print("   Without the private key, these tokens are completely unreadable!")


print("Researcher's Side: Decrypting received tokens...")
print()

decrypted_grades = []

for i, token in enumerate(encrypted_grades):

    # Decrypt using the researcher's PRIVATE key
    # Must use the same OAEP padding scheme as encryption
    clean_grade = private_key.decrypt(
        token,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    grade_int = int(clean_grade.decode())  # Decode bytes → string → integer
    decrypted_grades.append(grade_int)

    print(f"   Token [{i+1}] -> Decrypted Grade: {grade_int}")

print()
print("All tokens decrypted successfully!")