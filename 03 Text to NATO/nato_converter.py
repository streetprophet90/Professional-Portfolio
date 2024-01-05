# NATO Phonetic Alphabet Dictionary
NATO_PHONETIC_ALPHABET = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
    'Z': 'Zulu', ' ': 'Space'
}

def text_to_nato(text):
    nato_result = []
    for char in text.upper():
        if char in NATO_PHONETIC_ALPHABET:
            nato_result.append(NATO_PHONETIC_ALPHABET[char])
            nato_result.append(' ')
        else:
            nato_result.append(char)
            nato_result.append(' ')
    return ' '.join(nato_result)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    nato_result = text_to_nato(user_input)
    print(f"NATO Phonetic Alphabet: {nato_result} ")