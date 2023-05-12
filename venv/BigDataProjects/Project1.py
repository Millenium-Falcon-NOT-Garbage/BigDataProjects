from multiprocessing import Process, Queue
import random
from heapq import merge
from timer import Timer


bigList = []
listSize = 1000000
divNum = 5


for i in range(listSize):
    bigList.append(random.randint(0, 500000))

def split(inputList, div):
    splitList = []
    for i in range(div):
        splitList.append(inputList[i::div])

    return splitList

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

# def mergeSort(arr):
#     if len(arr) > 1:
#
#         # Finding the mid of the array
#         mid = len(arr) // 2
#
#         # Dividing the array elements
#         L = arr[:mid]
#
#         # into 2 halves
#         R = arr[mid:]
#
#         # Sorting the first half
#         mergeSort(L)
#
#         # Sorting the second half
#         mergeSort(R)
#
#         i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] <= R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

def workerSort(qin, qout):
    while not qin.empty():
        stack = qin.get()
        sort_set(stack)
        qout.put(stack)

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

    t = Timer("accumulate")
    t.start()
    print("*** CODE STARTS ***")
    print("Timer Began")

    inq = Queue()
    outq = Queue()

    new_list = split(bigList, 300)

    for lst in new_list:
        inq.put(lst)

    t.stop()
    print("\nSplitting List Done")
    t.start()

    sortProcesses = [Process(target=workerSort, args=(inq, outq,)) for i in range(5)]
    finalList = []

    for process in sortProcesses:
        process.start()

    t.stop()
    print("\nProcesses started")
    t.start()

    while len(finalList) < listSize:
        a = outq.get()
        if inq.empty():
            t.stop()
            print("In queue Done")
            t.start()
        finalList = merging(finalList, a)

    t.stop()
    print("\nlists merged")
    t.start()

    # for process in sortProcesses:
    #     process.join()

    # print(finalList)

    t.stop()
    print("\nProcesses joined.")
    print("*** CODE FINISHED ***")

    for process in sortProcesses:
        process.terminate()