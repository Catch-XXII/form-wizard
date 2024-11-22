from datetime import datetime

# Get the current date
current_date = datetime.now()

# Format the date as "22 November 2024"
formatted_date = current_date.strftime("%d %B,%Y")

print(formatted_date)
