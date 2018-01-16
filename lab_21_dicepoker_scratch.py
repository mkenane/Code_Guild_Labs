from random import randrange

def dielist():
    counts = [0, 0, 0, 0, 0]
    for die in range(5):
        counts[die] = randrange(1,7)
    return counts


sampleroll = [1, 4, 4, 6, 6]


def score():
    how_many = []
    for i in dice_list:
        occurences = dice_list.count(i)
        how_many.append(occurences)
    return how_many
print(count(sampleroll))


# def score():
#     how_many = []
#     counts = [0, 0, 0, 0, 0]
#     for die in range(5):
#         counts[die] = randrange(1,7)
#
#     for i in counts:
#         occurences = counts.count(i)
#         how_many.append(occurences)
#     return how_many
# print(score())
#
# for index in range(5):
#     self.dice[index] = randrange(1,7)
