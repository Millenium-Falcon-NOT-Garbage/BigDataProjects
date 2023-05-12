from multiprocessing import Process, Queue
import random
from timer import Timer
import dispy


bigList = []
listSize = 100000
divNum = 5


for i in range(listSize):
    bigList.append(random.randint(0, 500000))

def split(inputList, div):
    splitList = []
    for i in range(div):
        splitList.append(inputList[i::div])

    return splitList


def workerSort(bruh):

    def sort_set(arr):
        n = len(arr)
        swapped = False
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if not swapped:
                return

    sort_set(bruh)
    return bruh

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

    new_list = split(bigList, 300)

    t.stop()
    print("\nSplitting List Done")
    t.start()

    cluster = dispy.JobCluster(workerSort) #, nodes='192.168.0.*', host='192.168.0.1')
    jobs = []
    finalList = []

    for i in new_list:
        job = cluster.submit(i)
        print("Jobs submitted " + str(i))
        jobs.append(job)

    j = 0
    for job in jobs:
        n = job()
        print("Job done " + str(j))
        j+=1
        # print('%s executed job %s at %s with %s' % (host, job.id, job.start_time, n))
        finalList = merging(finalList, n)

    cluster.print_status()

    t.stop()
    print("\nlists merged")
    t.start()

    t.stop()
    print("\nProcesses joined.")
    print("*** CODE FINISHED ***")