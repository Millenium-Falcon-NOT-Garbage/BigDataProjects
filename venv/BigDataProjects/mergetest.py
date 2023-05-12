

def chunkMerge(file1, file2):

    path = '/Users/john/PycharmProject/BigDataLesson1/venv/BigDataProjects/'

    f1 = open(file1, 'r')
    f2 = open(file2, 'r')

    mergefile = open(path + "MERGE TEST", "a")

    line1 = f1.readline()
    line2 = f2.readline()

    while True:

        if not line1 and not line2:
            break
        else:
            if line1:
                v1 = int(line1)
            if line2:
                v2 = int(line2)

        v1 = int(line1)
        v2 = int(line2)

        print("file 1 val: %d" % v1)
        print("file 2 val: %d" % v2)

        if v1 < v2:
            mergefile.write(str(v1) + '\n')
            line1 = f1.readline()
        else:
            mergefile.write(str(v2) + '\n')
            line2 = f2.readline()

    f1.close()
    f2.close()

if __name__ == "__main__":

    file1 = "/Users/john/PycharmProject/BigDataLesson1/venv/BigDataProjects/large_file.set.0sorted"
    file2 = "/Users/john/PycharmProject/BigDataLesson1/venv/BigDataProjects/large_file.set.1sorted"

    chunkMerge(file1, file2)

