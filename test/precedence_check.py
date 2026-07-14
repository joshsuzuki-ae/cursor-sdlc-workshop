def add(a, b):
    # intentional trivial code for a PR diff
    result = a + b
    return result

def risky_divide(a, b):
    return a / b  # no zero check on purpose

if __name__ == "__main__":
    print(add(2, 3))
    print(risky_divide(10, 0))
