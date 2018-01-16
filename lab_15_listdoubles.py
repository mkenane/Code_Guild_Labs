

def doubles(lst, n):
    mulitpliedByN = [i * n for i in lst]
    deletedZeros = [x for x in mulitpliedByN if x != 0]
    return deletedZeros

print(doubles([1, 2, 0, 3, 4, 0, 5, 6], 2))
