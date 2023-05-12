from multiprocessing import Process, Queue
import random
from timer import Timer
import dispy
import os
import glob


def read_in_lines(file, num_lines = 6):
    count = 0
    data = []
    for line in file:
        count += 1
        data.append(line)
        if count == num_lines:
            count = 0
            yield data
            data.clear()


def split(inputList, div):
    splitList = []
    for i in range(div):
        splitList.append(inputList[i::div])

    return splitList


def workerSort(thefile):

    path = '/Users/john/PycharmProject/BigDataLesson1/venv/BigDataProjects/'
    # path = '/mnt/usb1'

    yay = []

    with open(thefile, 'r') as f:
        yay = [line.rstrip('\n') for line in f]

        print("********")
        print(yay)
        print("********")

        yay = [int(x) for x in yay]

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

    sort_set(yay)
    bigList = []
    bigList = merging(bigList, yay)

    # path = '/Users/john/PycharmProject/BigDataLesson1/venv/BigDataProjects/'

    with open(thefile + "sorted", 'w') as myfile:
        myfile.writelines([str(a) + "\n" for a in bigList])
    # myfile.close()


def testWorker():

    path = '/Users/john/PycharmProject/BigDataLesson1/venv/BigDataProjects/helpme'
    myfile = open(path, 'w')
    myfile.writelines("THANK YOU MR BAKKER")
    # myfile.writelines([str(a) for a in bigList])
    myfile.close()


if __name__ == "__main__":

    t = Timer("accumulate")
    t.start()
    print("*** CODE STARTS ***")
    print("Timer Began")

    # Splits large file up into smaller files that will be stored in nfs
    # l = 30 * 10 ** 5
    file_large = '/Users/john/PycharmProject/BigDataLesson1/venv/BigDataProjects/large_file.set'

    with open(file_large) as f:
        i = 0
        for piece in read_in_lines(f):
            file_split = '{}.{}'.format(file_large, str(i))
            i+=1
            with open(file_split, 'w') as g:
                g.writelines(piece)

    cluster = dispy.JobCluster(workerSort)
    print("Cluster created")

    jobs = []

    submission = 0
    for file in glob.glob("/Users/john/PycharmProject/BigDataLesson1/venv/BigDataProjects/large_file.set.*"):
        print(file)
        job = cluster.submit(file)
        print("Job Submitted " + str(submission))
        submission += 1
        jobs.append(job)
    # job = cluster.submit()
    #     with open(file, 'r') as f:
    #
    #         lst = [line.rstrip('\n') for line in f]
    #         print(lst)
    #
    #         lst = lst[0].split(', ')
    #
    #         print("********")
    #         print(lst)
    #         print("********")
    #
    #         lst = [int(x) for x in lst]
    #         print("*** CONVERT TO INT PLS ***")
    #         print(lst)
    #         print("*** CONVERT TO INT PLS ***")
    #
    #         job = cluster.submit(lst)
    #         print("Job Submitted " + str(submission))
    #         submission += 1
    #         jobs.append(job)

    j = 0
    for job in jobs:
        n = job()
        print("Job done " + str(j))
        j += 1

    cluster.print_status()

    t.stop()
    print("\nlists merged")
    print("*** CODE FINISHED ***")