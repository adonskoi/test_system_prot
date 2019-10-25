from .first import FirstCase
from .second import SecondCase


def main():
    case = FirstCase(1, "first name")
    case.execute()
    print("\n")
    case2 = SecondCase(22, "second name")
    case2.execute()
    print("\n")


if __name__ == "__main__":
    main()
