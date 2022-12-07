import time

my_characters = {
    "a": "01100001",
    "b": "01100010",
    "c": "01100011",
    "d": "01100100",
    "e": "01100101",
    "f": "01100110",
    "g": "01100111",
    "h": "01101000",
    "i": "01101001",
    "j": "01101010",
    "k": "01101011",
    "l": "01101100",
    "m": "01101101",
    "n": "01101110",
    "o": "01101111",
    "p": "01110000",
    "q": "01110001",
    "r": "01110010",
    "s": "01110011",
    "t": "01110100",
    "u": "01110101",
    "v": "01110110",
    "w": "01110111",
    "x": "01111000",
    "y": "01111001",
    "z": "01111010",
    " ": "01000000"
}

def convert(word):
    words = word
    character_storage = []
    converted_charater = []
    joined_character = ""

    for char in words:
        character_storage.append(char)
    for n in range(len(character_storage)):
        for key, value in my_characters.items():
            if character_storage[n] == key:
                converted_charater.append(value)
    for conv in converted_charater:
        joined_character += conv + " "
    return [words, joined_character]

def display(words, joined_character):
    print("Please wait while we convert your text ")
    time.sleep(2)
    print(f'We are converting "{words}" ')
    time.sleep(2)
    print(f"Converted To: {joined_character}")



if __name__=="__main__":
    print("Welcome To Bestz Text To Binary Converter")
    time.sleep(2)
    print('Write a message and we would convert it to binary number')
    time.sleep(2)
    user_input = input('Write Text: ').lower()
    show = convert(user_input)
    display(show[0], show[1])

