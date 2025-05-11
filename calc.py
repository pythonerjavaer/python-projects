def divide(a, b):
    result = a / b
    return result

def main():
    x = 10
    y = 0     # ❌ 故意制造除零错误
    z = divide(x, y)
    print("Result:", z)

if __name__ == "__main__":
    main()