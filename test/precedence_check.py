def add(a, b):
    # intentional trivial code for a PR diff
    result = a + b
    return result

def risky_divide(a, b):
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    print(add(2, 3))
    print(risky_divide(10, 0))

def multiply(a, b):
    return a * b  # new change to trigger a fresh push
