def main():
    # len()関数の例
    hensu = len("abcde")
    print("len()の例1:" + str(hensu))

    hensu = len([1, 3, 5])
    print("len()の例2:" + str(hensu))

    hensu = len({"key1": "value1", "key2": "value2"})
    print("len()の例3:" + str(hensu))

    # abs()関数の例
    hensu = abs(100)
    print("abs()の例1:" + str(hensu))

    hensu = abs(-100)
    print("abs()の例2:" + str(hensu))


if __name__ == "__main__":
    main()
