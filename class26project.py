import random
import string
def generate_password(length=random.randint(1,15), use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters+=string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password
print(generate_password())