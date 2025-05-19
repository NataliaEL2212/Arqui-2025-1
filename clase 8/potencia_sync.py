import time

def power(n):
    result = 1
    for _ in range(n):
        result *= n
    return result

def main():
    n = 100_000
    start = time.time()
    power(n)
    end = time.time()
    print(f"Synchronous power calculation took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
