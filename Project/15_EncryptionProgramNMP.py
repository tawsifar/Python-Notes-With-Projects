import random
import string

# ---------------------------------------------------------
# Build the full set of characters we want to be able to
# encrypt/decrypt: a space, punctuation, digits, and letters.
# ---------------------------------------------------------
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)  # convert string to a list, so we can use .index() and shuffle

# ---------------------------------------------------------
# Create the "key" — a shuffled copy of chars.
# chars[i] will map to key[i] for encryption,
# and key[i] will map back to chars[i] for decryption.
# ---------------------------------------------------------
key = chars.copy()      # copy so shuffling key doesn't affect chars
random.shuffle(key)     # randomly reorder the key list


def encrypt(plain_text):
    """Encrypt plain_text using the chars -> key mapping."""
    cipher_text = ""
    for letter in plain_text:
        # find where this letter sits in chars
        index = chars.index(letter)
        # replace it with the letter at the same position in key
        cipher_text += key[index]
    return cipher_text


def decrypt(cipher_text):
    """Decrypt cipher_text using the key -> chars mapping (reverse of encrypt)."""
    plain_text = ""
    for letter in cipher_text:
        # find where this letter sits in key
        index = key.index(letter)
        # replace it with the letter at the same position in chars
        plain_text += chars[index]
    return plain_text


def main():
    # ----------------- ENCRYPT -----------------
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = encrypt(plain_text)

    print(f"original message : {plain_text}")
    print(f"encrypted message: {cipher_text}")

    # ----------------- DECRYPT -----------------
    # Re-decrypt the cipher_text we just created (same key, same session)
    decrypted_text = decrypt(cipher_text)

    print(f"encrypted message: {cipher_text}")
    print(f"original message : {decrypted_text}")


if __name__ == '__main__':
    main()