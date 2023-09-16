from mylib1 import mylib1_kansu1
from mylib.mylib2 import mylib2_kansu2


def main():
    mylib1_kansu1()
    # importしてないので使えない
    # mylib1.mylib1_kansu2()

    # importしていないので使えない
    # mylib.mylib2.mylib2_kansu1()
    mylib2_kansu2()


if __name__ == "__main__":
    main()
