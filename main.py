import subprocess
from random import randint as rand

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

def convert(word):
	global convertedSentence, alphabet
	converted = ""
	doubleT = doubleT_Presence = th_Presence = False
	for i in range(len(word)):
		if doubleT or th_Presence:
			doubleT = th_Presence = False
			continue
		elif ((word[i] == "L" or word[i] == "l") and not doubleT_Presence) or (word[i] == "R" or word[i] == "r"):
			converted += "W" if word[i].isupper() else "w"
		elif (word[i] == "T" or word[i] == "t") and ((word[i + (1 if i + 1 < len(word) else 0)] == "T" or word[i + (1 if i + 1 < len(word) else 0)] == "t")):
			converted += (("D" if word[i].isupper() else "d") + ("D" if word[i + 1].isupper() else "d")) if i + 1 < len(word) else "t"
			doubleT = doubleT_Presence = True if i + 1 < len(word) else False
		elif (word[i] == "T" or word[i] == "t") and ((word[i + (1 if i + 1 < len(word) else 0)] == "H" or word[i + (1 if i + 1 < len(word) else 0)] == "h")):
			converted += ("F" if word[i].isupper() else "f") if i + 2 == len(word) else "t"
			th_Presence = True if i + 2 == len(word) else False
		else:
			converted += word[i]
	convertedSentence += ((converted[0] + "-" + converted[0:]) if (rand(1, 10) == 1 and converted[0] in alphabet) else converted) + " "

while True: # TURN THIS TO TRUE
	option = int(input("1. String\n2. Text File\nEnter Option here: "))
	if option == 2:
		fName = input("Enter the name of your file (with extension): ")
		text = open("INPUT/" + fName, "r").read().strip().split('\n')
	elif option == 1:
		userInput = input("Enter Text Here: ")
	else:
		print("Please enter in a valid option!!\n\n")
		continue
	break

convertedSentence = ""
if option == 1:
	words = userInput.split(" ")
	for i in words:
		convert(i)
else:
	for i in text:
		temp = i.split(" ")
		for n in temp:
			convert(n)
		convertedSentence += "\n"
	UwU = open("OUTPUT/" + fName.split(".")[0] + "_UwU.txt", "w")
	UwU.write(convertedSentence)

print("\n" + convertedSentence)
#subprocess.call(["espeak", "" + convertedSentence]) # this is for text to speech, leave commented