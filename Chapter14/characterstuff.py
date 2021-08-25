import string
import secrets

password_length = 16

def character():
    realm = [
        string.punctuation,
        string.ascii_letters
    ]
    return secrets.choice(realm[secrets.choice([1,0])])

print(f"New password is: {''.join([character() for _ in range(password_length)])}")