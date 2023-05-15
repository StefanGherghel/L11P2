import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time
import random

vect = []
dim = 1000
for i in range(0, dim):
    vect.append(random.randint(0,dim))


def sortare(index1, index2, v):
    cv = []
    for i in range(index1, index2):
        cv.append(v[i])
    cv.sort()
    print(cv)


def ver_1():
    ind = int(dim/2)
    thread_1 = threading.Thread(target=sortare(0,ind,vect))
    thread_2 = threading.Thread(target=sortare(ind+1, dim, vect))
    thread_1.start()
    thread_2.start()
    rez1 = thread_1.join()
    rez2 = thread_2.join()



def ver_2():
    ind = int(dim / 2)
    sortare(0, ind, vect)
    sortare(ind, dim, vect)


def ver_3():
    ind = int(dim / 2)
    process_1 = multiprocessing.Process(target=sortare(0,ind,vect))
    process_2 = multiprocessing.Process(target=sortare(ind+1, dim, vect))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()


def ver_4():
    ind = int(dim / 2)
    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(sortare(0, ind, vect))
        future = executor.submit(sortare(ind+1, dim, vect))


if __name__ == '__main__':
    start = time.time()
    ver_1()
    end = time.time()
    print("\n Timp executie pseudoparalelism cu GIL")
    print(end - start)
    start = time.time()
    ver_2()
    end = time.time()
    print("\n Timp executie secvential")
    print(end - start)
    start = time.time()
    ver_3()
    end = time.time()
    print("\n Timp executie paralela cu multiprocessing")
    print(end - start)
    start = time.time()
    ver_4()
    end = time.time()
    print("\n Timp executie paralela cu concurrent.futures")
    print(end - start)
