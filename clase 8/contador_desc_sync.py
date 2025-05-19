import time

def countdown(n):
    while n > 0:
        n -= 1

def main():
    start = time.time()
    countdown(100_000_000)
    end = time.time()
    print(f"Synchronous countdown took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
