import itertools
import hashlib

# Define the keys used in the password
keys = ['a', 'd', 'e', 'g', 'i', 'k', 'l', 'r', 's']

# Target MD5 hash
target_hash = "53ba4c338b0578878240cff683fa9a1d"

# Brute force approach to generate all possible combinations
def crack_password():
    # Start by including at least one of each letter
    base_password = ''.join(keys)
    remaining_length = 13 - len(base_password)  # Determine the remaining characters needed

    # Generate all possible combinations of the remaining length
    for combination in itertools.product(keys, repeat=remaining_length):
        # Add the additional characters to the base password
        candidate = base_password + ''.join(combination)

        # Generate all permutations of the 13-character string
        for permutation in itertools.permutations(candidate, 13):
            password = ''.join(permutation)
            # Compute the MD5 hash
            password_hash = hashlib.md5(password.encode()).hexdigest()
            # Check if it matches the target hash
            if password_hash == target_hash:
                return password  # Return the password if found

    return None  # Return None if no match is found

# Run the script
if __name__ == "__main__":
    password = crack_password()
    if password:
        print(f"Password found: {password}")
    else:
        print("Password not found.")
