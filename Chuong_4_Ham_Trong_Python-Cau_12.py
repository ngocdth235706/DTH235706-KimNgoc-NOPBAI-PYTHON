def oscillate(start, stop):
    """Generator: for n in range(start, stop) yield n then -n"""
    for n in range(start, stop):
        yield n
        yield -n

if __name__ == "__main__":
    for n in oscillate(-3, 5):
        print(n, end=' ')
    print()

def oscillate(start, stop):
    """Generator: for n in range(start, stop) yield n then -n"""
    for n in range(start, stop):
        yield n
        yield -n

if __name__ == "__main__":
    for n in oscillate(-3, 5):
        print(n, end=' ')
    print()