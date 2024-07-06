import re

def normalize_phone(phone_number: str):
    pattern = r"[^+\d]"
    number = re.sub(pattern, '', phone_number)

    # match = re.search(r"(\+)?(38)?(\d+)", number)
    # number = match.group(1) if match.group(1) else "+"
    # number += match.group(2) if match.group(2) else "38"
    # number += match.group(3)
    ## print(match.group(1), match.group(2), match.group(3))

    number = re.sub(r"(\+)?(38)?(\d{6})", r"+38\3", number)

    return number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
