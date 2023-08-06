# IndexError の例
def main():
    func_a()
    print()


def func_a():
    areas = ["北海道", "青森", "秋田"]
    for i in range(4):
        print(areas[i])


if __name__ == "__main__":
    main()
