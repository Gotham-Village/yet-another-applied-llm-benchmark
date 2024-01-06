from evaluator import *

TAGS = ['bash']

question = 'In bash how do I list all files in foo/ but sort the files by the least significant digit of their size so 2820 comes first and then 281771 and finally 2279. I want just the file names.'


def setup_fn():
    sizes = [921, 714, 120, 637, 366, 662, 305, 403, 49, 158]
    
    import os
    import time
    os.mkdir("foo")
    time.sleep(.5)
 
    for i, size in enumerate(sizes):
        with open("foo/{}".format(i), "w") as f:
            f.write("a"*size)

    time.sleep(.5)

def fix_whitespace(x):
    return " ".join(x.split())


TestBashListSize = Setup(setup_fn) >> question >> LLMRun() >> ExtractCode() >> BashRun() >> PyFunc(fix_whitespace) >> EqualEvaluator("2 0 5 7 1 6 4 3 9 8")


if __name__ == "__main__":
    print(run_test(TestBashListSize))

