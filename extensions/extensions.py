### Output filetype after user types in filename ###

filename = input("File name: ").lower().strip()

if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpg"):
    print("image/jpg")
        