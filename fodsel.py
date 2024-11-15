import hashlib
from datetime import datetime, timedelta

# The given hash
target_hash = "06cd97558029ae3a9e1f7fcdcd74771d"

def calculate_control_digits(fodselsnummer):
    """
    Calculate the two control digits for a given fødselsnummer (first 9 digits).
    """
    weights1 = [3, 7, 6, 1, 8, 9, 4, 5, 2]
    weights2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    # First control digit
    d1 = sum(int(fodselsnummer[i]) * weights1[i] for i in range(9)) % 11
    d1 = 0 if d1 == 0 else 11 - d1
    if d1 == 10:
        return None  # Invalid fødselsnummer

    # Second control digit
    fodselsnummer += str(d1)
    d2 = sum(int(fodselsnummer[i]) * weights2[i] for i in range(10)) % 11
    d2 = 0 if d2 == 0 else 11 - d2
    if d2 == 10:
        return None  # Invalid fødselsnummer

    return str(d1) + str(d2)

def generate_fodselsnummer(start_year, end_year):
    """
    Generate all valid fødselsnummer combinations for a given year range.
    """
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date

    for day in range(delta.days + 1):
        current_date = start_date + timedelta(days=day)
        ddmmyy = current_date.strftime("%d%m%y")
        for individ in range(0, 1000):  # Individual number from 000 to 999
            individ_number = f"{individ:03d}"
            partial_fodselsnummer = ddmmyy + individ_number
            control_digits = calculate_control_digits(partial_fodselsnummer)
            if control_digits:
                yield partial_fodselsnummer + control_digits

def crack_hash(target_hash, start_year, end_year):
    """
    Brute force the given hash using generated fødselsnummer combinations.
    """
    for fodselsnummer in generate_fodselsnummer(start_year, end_year):
        hashed = hashlib.md5(fodselsnummer.encode()).hexdigest()
        if hashed == target_hash:
            print(f"Match found: {fodselsnummer}")
            return fodselsnummer
    print("No match found.")
    return None

# Run the script for a specific year range
if __name__ == "__main__":
    start_year = 1900
    end_year = 2024
    result = crack_hash(target_hash, start_year, end_year)
