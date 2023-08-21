def main():
    # 足し算の機能を定義
    def tashizan(hikisu1, hikisu2):
        # 引数１と引数２を足して、結果をリターンする
        kekka = hikisu1 + hikisu2
        return kekka

    # 足し算の結果を表示するメイン処理
    hensu = tashizan(1, 1)
    print(hensu)  # 2

    hensu = tashizan(2, 5)
    print(hensu)  # 7

    hensu = tashizan(3, 7)
    print(hensu)  # 10


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
    kekka = hikisu + hikisu
    return kekka


# 使い方３
hensu = kansu3(2)

if __name__ == "__main__":
    main()
