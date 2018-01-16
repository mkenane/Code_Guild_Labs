inputTime = input("please insert the current time of day in the following format hh:mm:pm (for example 03:45:PM) : ")

convertedTime = int(inputTime[:1])
amorpm = inputTime[-2:].lower()

if 7 <= convertedTime < 9 and amorpm[0] == "a":
    print("it is breakfast time!")

elif (convertedTime == 12 or convertedTime == 1) and amorpm[0] == "p":
    print("it is lunch time!")

elif 7 <= convertedTime < 9 and amorpm[0] == "p":
    print("it is dinner time!")

elif ( 10 <= convertedTime < 12 or 1 <= convertedTime < 4) and amorpm[0] == "a":
    print("it is hammer time!")

else:
    print("stop eating!")


# if I wanted to user fool-proof this, would need to add these statements:
# timesplit = inputTime.split(":")
# if len(timesplit) > 3 and timesplit[0].isdigit() and timesplit[1].isdigit() and (timesplit[2].lower() == "am" or timesplit[2].lower() == "pm"):
