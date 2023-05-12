import glob, os

for f in glob.glob("/Users/john/PycharmProject/BigDataLesson1/venv/BigDataProjects/large_file.set.*"):
    os.remove(f)



# from multiprocessing import Process, Queue
# import time
# import random
#
# def func(x, i):
#     while True:
#         r = random.randint(1, 2)
#         message = x.get()
#         if message == "done":
#             print("{} process exiting...".format(i))
#             break
#         print("{} Message: {}" .format(i, message))
#         time.sleep(r)
#
# if __name__ == '__main__':
#
#     q = Queue()
#     for i in range(1, 51):
#        q.put(i)
#
#     myp = []
#     for i in range(5):
#         q.put("done")
#         p = Process(target=func, args=(q,i))
#         p.start()
#         myp.append((p))
#
#     for process in myp:
#         process.join()
#
#
