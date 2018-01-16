englishword = input("insert one single word to translate to Pig Latin: ")


if englishword[0] in "aeiou":
    print(englishword + "yay")
else:
    print(englishword[1:] + englishword[0] + "ay")

    
