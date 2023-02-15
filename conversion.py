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
    "A": "01000001",
    "B": "01000010",
    "C": "01000011",
    "D": "01000100",
    "E": "01000101",
    "F": "01000110",
    "G": "01000111",
    "H": "01001000",
    "I": "01001001",
    "J": "01001010",
    "K": "01001011",
    "L": "01001100",
    "M": "01001101",
    "N": "01001110",
    "O": "01001111",
    "P": "01010000",
    "Q": "01010001",
    "R": "01010010",
    "S": "01010011",
    "T": "01010100",
    "U": "01010101",
    "V": "01010110",
    "W": "01010111",
    "X": "01011000",
    "Y": "01011001",
    "Z": "01011010",
    " ": "01000000",
    ",": "00101100",
    ".": "00101110"
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
    user_input = input('Write Text: ')
    show = convert(user_input)
    display(show[0], show[1])

