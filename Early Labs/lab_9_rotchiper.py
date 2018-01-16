
import string
wordToEncode = input('please enter word: ')

abcRegular = " abcdefghijklmnopqrstuvwxyz"
abcRot13 = " nopqrstuvwxyzabcdefghijklm"
keyTable = str.maketrans(abcRegular, abcRot13)

encodedResult = wordToEncode.translate(keyTable)

print(encodedResult)
