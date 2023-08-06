# ZeroDivisionError の例
def main():
    d = func_a()
    l = func_b()

    print(d["key1"])
    print(d["key4"])

    print(l[0])
    print(l[4])


def func_a():
    d = {"key1": "value1", "key2": "value2", "key3": "value3"}
    return d


def func_b():
    l = ["index1", "index2", "index3"]
    return l


if __name__ == "__main__":
    main()
