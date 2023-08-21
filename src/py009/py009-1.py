def main():
    # 定義の仕方１
    # 引数なし/戻り値なし
    def kansu1():
        ...

    # 使い方１
    kansu1()

    # 定義の仕方２
    # 引数あり/戻り値なし
    def kansu2(hikisu):
        ...

    # 使い方２
    kansu2(1)

    # 定義の仕方３
    # 引数あり/戻り値あり
    def kansu3(hikisu):
        kekka = None
        return kekka

    # 使い方３
    hensu = kansu3(2)
    print(hensu)

    # 定義の仕方４
    # 引数あり(たくさん)/戻り値(1つ)あり
    def kansu4(hikisu1, hikisu2, hikisu3):
        kekka = None
        return kekka

    # 使い方４
    hensu = kansu4(1, 2, 3)
    print(hensu)


if __name__ == "__main__":
    main()
