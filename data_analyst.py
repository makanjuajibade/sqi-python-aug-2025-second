import re

def read_reviews(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        contents = f.read()
        return contents
    
text = read_reviews("reviews.txt")

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
all_emails = re.findall(pattern, text)
print(all_emails)


def save_emails(emails, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")  

save_emails(all_emails, "emails.txt")

phone_pattern = r"(?:\+234|234|0)[\s-]?(?:\d{3}[\s-]?\d{3}[\s-]?\d{4})"
all_phone_nos = re.findall(phone_pattern, text)
print(all_phone_nos)

def save_phone_nos(phone_numbers, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for number in phone_numbers:
            f.write(number + "\n")  

save_phone_nos(all_phone_nos, "phone_numbers.txt")
print(text)