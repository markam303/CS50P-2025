### Remove vowels from strings ###

def main():
    text = input("Input: ")
    removed_vowels = remove(text)
    print(removed_vowels)

def remove(text):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for i in vowels:
        text = text.replace(i, "")
    return text


main()