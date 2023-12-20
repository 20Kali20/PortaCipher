def porta_cipher(text, key):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for char in text:
        if char.isalpha():
            shift = alphabet.index(key.upper()) + 1
            if char.isupper():
                result += alphabet[(alphabet.index(char) + shift) % 26]
            else:
                result += alphabet[(alphabet.index(char.upper()) + shift) % 26].lower()
        else:
            result += char

    return result
