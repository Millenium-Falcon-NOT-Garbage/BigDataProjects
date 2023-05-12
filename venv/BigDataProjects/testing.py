import glob

def sort_set(lst):
    n = len(lst)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not swapped:
            return


def merging(firstList, secondList):
    ikey1 = 0
    ikey2 = 0

    result = []

    while ikey1 < len(firstList) and ikey2 < len(secondList):
        if firstList[ikey1] == secondList[ikey2]:
            result.append(firstList[ikey1])
            result.append(secondList[ikey2])
            ikey1 += 1
            ikey2 += 1
        elif firstList[ikey1] < secondList[ikey2]:
            result.append(firstList[ikey1])
            ikey1 += 1
        else:
            result.append(secondList[ikey2])
            ikey2 += 1

    if (ikey1 == len(firstList)) and (ikey2 < len(secondList)):
        result.extend(secondList[ikey2:])
    elif (ikey1 < len(firstList)) and (ikey2 == len(secondList)):
        result.extend(firstList[ikey1:])

    return result

if __name__ == "__main__":

    file = "/Users/john/PycharmProject/BigDataLesson1/venv/BigDataProjects/large_file.set.0"
    yay = []
    with open(file, 'r') as f:
        yay = [line.rstrip('\n') for line in f]

        print("********")
        print(yay)
        print("********")

        yay = [int(x) for x in yay]

    sort_set(yay)
    bigList = []
    bigList = merging(bigList, yay)

    with open(file + "sorted", 'w') as myfile:
        myfile.writelines([str(a) + "\n" for a in yay])
    # myfile.close()