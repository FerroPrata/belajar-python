import random
import string

def generate_unique_id():
    characters = string.ascii_letters + string.digits
    unique_id = ''.join(random.choice(characters) for _ in range(8))
    return unique_id

stru = str(generate_unique_id())


