#Given input String of combination of the lower and upper case ,arrange characters in such a way that all lowercase letters should come first.

inputStr = "AshIRbaD"
words = inputStr.split()     #split for splitting the string
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print("\n arranging characters first  lowercase letters and the uppercase ones:")
print(sortedString)