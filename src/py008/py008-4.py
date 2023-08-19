def main():
    # 4. 変数の値を入れ替えてみる
    # 変数を定義
    hensu1 = None
    hensu2 = None

    # これはNone
    print(hensu1)
    print(hensu2)

    # 変数に値を入れる
    hensu1 = 1
    hensu2 = 2
    # これは上記の値が表示される
    print(hensu1)
    print(hensu2)

    # 変数の値を入れ替える
    hensu1 = 1 + 1
    hensu2 = 2 + 2
    # これは、入れなおした値が表示される
    print(hensu1)
    print(hensu2)


# これ以下はおまじない（とりあえず丸暗記）
if __name__ == "__main__":
    main()
