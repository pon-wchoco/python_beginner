def main():
    # 型の決め方

    # 文字列型
    mojiretsu_gata = "abc"

    kata = type(mojiretsu_gata)
    print(kata)

    # 整数型
    seisu_gata = 100
    kata = type(seisu_gata)
    print(kata)

    # 配列型
    hairetsu_gata = [1, 2, 3]
    kata = type(hairetsu_gata)
    print(kata)

    # 辞書型
    jisho_gata = {"key1": "value1", "key2": "value2", "key3": "value3"}
    kata = type(jisho_gata)
    print(kata)

    # ブール型(True か False だけ)
    bool_gata = True
    kata = type(bool_gata)
    print(kata)

    # タプル型
    tuple_gata = ("value1", "value2")
    kata = type(tuple_gata)
    print(kata)


if __name__ == "__main__":
    main()
