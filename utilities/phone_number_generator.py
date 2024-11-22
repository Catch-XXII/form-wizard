import secrets


def generate_phone_number(num_digits=10) -> str:
    if num_digits <= 0:
        raise ValueError("Number of digits must be greater than 0.")
    return "".join(str(secrets.randbelow(10)) for _ in range(num_digits))
