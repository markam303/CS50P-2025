### Convert str to emoji ###
#
import emoji

words = input("Input: ")
print("Output:", emoji.emojize(words, language='alias'))