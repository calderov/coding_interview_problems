import os
import random

def GetRandomFile(basepath):
    pending = [os.path.join(basepath, item) for item in os.listdir(basepath)]
    files = []

    while pending:
        if os.path.isfile(pending[-1]):
            files.append(pending.pop())
        else:
            currentDir = pending.pop()
            dirItems = [os.path.join(currentDir, item) for item in os.listdir(currentDir)]
            for item in dirItems:
                pending.append(item)

    return random.sample(files, 1)[0]

if __name__ == "__main__":
    basepath = "C:\\git\\grokking_the_coding_interview\\Exercises\\"
    randomProblem = GetRandomFile(basepath)
    print("Opening", randomProblem)
    os.popen("code " + randomProblem)
    print("Done")