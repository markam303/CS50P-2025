### Remove vowels from strings ###

def main():
    text = input("Input: ")
    removed_vowels = shorten(text)
    print(f"Output: {removed_vowels}")

def shorten(text):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for i in vowels:
        text = text.replace(i, "")
    return text


if __name__ == "__main__":
    main()