sampleText = """To see a long bridge dilapidated, and mysteriously winding
into darkness, profound melancholy over the loss of dearest
possessions and dismal situations will fall upon you.
To the young and those in love, disappointment in the heart's
fondest hopes, as the loved one will fall below your ideal.

To cross a bridge safely, a final surmounting of difficulties,
though the means seem hardly safe to use.  Any obstacle
or delay denotes disaster.

To see a bridge give way before you, beware of treachery and false admirers.
Affluence comes with clear waters.  Sorrowful returns of best efforts are
experienced after looking upon or coming in contact with muddy or turbid
water in dreams."""

from collections import Counter
from operator import itemgetter
# booktext = open('book.txt', "r+")
# insanity = booktext.read()
# booktext.close()

# manual string manipulation
stringManipulation1 = sampleText.replace(",", " ")
stringManipulation2 = stringManipulation1.replace(".", " ")
stringManipulation3 = stringManipulation2.replace("-", " ")

sampleTextIntoList = (stringManipulation3.lower()).split()
#removePunctuation = [word.rstip([-1] if word[-1] in ".,':;)!?-") else word for word in sampleTextIntoList]

countingEachWord = [sampleTextIntoList.count(word) for word in sampleTextIntoList]
wordCountDictionary = dict(zip(sampleTextIntoList, countingEachWord))

dictionaryIntoList = list(wordCountDictionary.items())

sortedDictionary  = sorted(dictionaryIntoList, key=itemgetter(1), reverse=True)


print(sortedDictionary)
