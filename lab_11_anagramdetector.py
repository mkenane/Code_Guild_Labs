

def anagramdetect(word1, word2):
    letterSplit1 = sorted(list(word1.replace(' ', '').lower()))
    letterSplit2 = sorted(list(word2.replace(' ', '').lower()))
    if letterSplit1 == letterSplit2:
        return ("these words are anagrams")
    else:
        return "words are not anagrams"

print(anagramdetect("Madam", "Radium came"))
