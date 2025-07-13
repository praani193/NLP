import re

text = "Contact us at support@example.com. The event is on 12-05-2024."
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
date_pattern = r"\b\d{2}-\d{2}-\d{4}\b"
emails = re.findall(email_pattern, text)
dates = re.findall(date_pattern, text)

print("Emails:", emails)
print("Dates:", dates)
