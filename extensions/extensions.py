### Output filetype after user types in filename ###

filename = input("File name: ").lower().strip()

match filename:
    case filename.endswith(".gif"):
        print("image/gif")