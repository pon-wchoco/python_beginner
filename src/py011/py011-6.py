# ループや分岐はスコープにならない！
def main():
    hensu_main = "メイン変数"

    # 関数
    def kansu():
        hensu_main = "メイン（関数の内側）"
        print(hensu_main)

    # ループ
    for i in range(3):
        hensu_loop = "ループ"
        hensu_main = "メイン（ループの内側）"
        print(str(i) + ":" + hensu_loop + "," + hensu_main)

    # 分岐
    if True:
        hensu_bunki = "分岐"
        hensu_main = "メイン（分岐の内側）"
        print(hensu_bunki + "," + hensu_main)

    kansu()

    print(hensu_main)
    # 以下は他スコープの内側の変数の様に見えるが、使えてしまう
    print(hensu_loop)
    print(hensu_bunki)


if __name__ == "__main__":
    main()
