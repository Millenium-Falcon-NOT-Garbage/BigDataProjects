
import random

a = -1000000
b = 1000000

testCases = {}

y = 9

for x in range(y):
    testCases['Case ' + str(x)] = [random.randint(a, b), random.randint(a, b), random.randint(a, b),
                                   random.randint(a, b), random.randint(a, b), random.randint(a, b),
                                   random.randint(a, b), random.randint(a, b)]
    testCases['Answer ' + str(x)] = sorted(testCases['Case ' + str(x)])


def sort_set(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


if __name__ == "__main__":

    for length in range(y):

        i = (int(len(testCases['Case ' + str(length)]) / 2))
        keys1 = testCases['Case ' + str(length)][:i]
        keys2 = testCases['Case ' + str(length)][i:]

        ikey1 = 0
        ikey2 = 0

        sort_set(keys1)
        sort_set(keys2)

        result = []

        while ikey1 < len(keys1) and ikey2 < len(keys2):
            if keys1[ikey1] < keys2[ikey2]:
                result.append(keys1[ikey1])
                ikey1 += 1
            else:
                result.append(keys2[ikey2])
                ikey2 += 1


        if(ikey1 == len(keys1)) and (ikey2 < len(keys2)):
            result.extend(keys2[ikey2:])
        else:
            result.extend(keys1[ikey1:])

        print("*" * 10)
        if testCases['Answer ' + str(length)] == result:
            print("Correct!")
        else:
            print("Incorrect!")
        print(result)

