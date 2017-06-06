
def checkio(mediantobe):

    if len(mediantobe) % 2 == 0:
        mediantobe.sort()
        FirstNumber = mediantobe[int((len(mediantobe)/2) - 1)]
        SecondNumber = mediantobe[int(len(mediantobe)/2)]
        median = (FirstNumber + SecondNumber) / 2
        return median

    else:
        mediantobe.sort()
        midpoint = len(mediantobe)/2
        print(midpoint)
        median = mediantobe[int(midpoint)]
        print(median)
        return median

print(checkio([1,2,3,4,5]))
