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


if __name__ == "__main__":
    main()
