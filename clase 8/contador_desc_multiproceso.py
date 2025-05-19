import time
from multiprocessing import Process

def countdown(n):
    while n > 0:
        n -= 1

def main():
    n = 100_000_000
    start = time.time()

    p1 = Process(target=countdown, args=(n // 2,))
    p2 = Process(target=countdown, args=(n // 2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print(f"Multiprocessing countdown took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
