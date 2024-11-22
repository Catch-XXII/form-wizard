import secrets
from datetime import datetime


def generate_phone_number(num_digits=10) -> str:
    if num_digits <= 0:
        raise ValueError("Number of digits must be greater than 0.")
    return "".join(str(secrets.randbelow(10)) for _ in range(num_digits))


# Get the current date
current_date = datetime.now()

# Format the date as "22 November 2024"
formatted_date = current_date.strftime("%d %B,%Y")

print(formatted_date)
