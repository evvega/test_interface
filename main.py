from classA import testA
from classB import testB


def main():
    a = testA()
    result = a.dormir()
    b = testB()
    result2 = b.comer()

    print(result)
    print(result2)


if __name__ == "__main__":
    main()
