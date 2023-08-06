# デバッグの例
def main():
    # 辞書オブジェクトを受け取る
    d = func_a()

    # リストオブジェクトを受け取る
    l = func_b()

    print("break point確認１")
    print("break point確認２")

    # 辞書オブジェクトの値を表示する
    print(d["key1"])
    print(d["key4"])

    # リストオブジェクトの値を表示する
    print(l[0])
    print(l[4])


def func_a():
    # 辞書オブジェクトを返す関数
    d = {"key1": "value1", "key2": "value2", "key3": "value3"}
    return d


def func_b():
    # リストオブジェクトを返す関数
    l = ["index1", "index2", "index3"]
    return l


if __name__ == "__main__":
    main()
