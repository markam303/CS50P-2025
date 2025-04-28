### Convert str to emoji ###
from emoji import emojize # type: ignore

text = input("Input: ")
print(emojize(text))
