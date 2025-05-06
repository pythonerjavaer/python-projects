import sys

def print_next_even_numbers(n: int, k: int):
    count = 0
    number = 2
    skipped = 0

    while count < n :
        if skipped < k:
            skipped += 1
        else:
            print(number)
            count += 1
        
        number += 2

def main(argv:list[str]):
    if len(argv) < 2:
        print("Usage: python3 evens.py <n> [<k>]")
        return
    
    n = int(argv[1])
    k = int(argv[2]) if len(argv) > 2 else 0
    print_next_even_numbers(n, k)

if __name__ == "__main__":
    main(sys.argv)