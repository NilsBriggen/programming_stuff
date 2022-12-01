import time
from multiprocessing import Pool

operations = ["+", "-", "*", "/"]
terms = {
    "(((str(a) + operation + str(b)) + operation1 + str(c)) + operation2 + str(d))",
    "((str(a) + operation + str(b)) + operation1 + str(c) + operation2 + str(d))",
    "((str(a) + operation + str(b) + operation1 + str(c)) + operation2 + str(d))",
    "(str(a) + operation + ((str(b) + operation1 + str(c)) + operation2 + str(d)))",
    "((str(a) + operation + str(b)) + operation1 + (str(c) + operation2 + str(d)))",
    "(str(a) + operation + (str(b) + operation1 + (str(c) + operation2 + str(d))))",
}

already_found = []


def calc(a, b, c, d):
    for operation in operations:
        for operation1 in operations:
            for operation2 in operations:
                for item in terms:
                    result = eval(item)
                    if result not in already_found:
                        result = eval(result)
                        if result == 24:
                            time.sleep(0.2)
                            already_found.append(eval(item))
                            #exec("print("+item+", '=', result)")


def start(x):
    for a in range(x-3, x):
        for b in range(x-3, x):
            for c in range(x-3, x):
                for d in range(x-3, x):
                    calc(a, b, c, d)

calcs = [4, 6, 8, 10, 12, 14]

if __name__ == '__main__':
    pool = Pool(processes=6)
    pool.map(start, calcs)
    pool.close()
    pool.join()
    print(already_found, "\n", len(already_found))
