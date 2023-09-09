# 内側のスコープで書き換えても外側のスコープに影響しない
def main():
    hensu_main = "メイン変数"

    def scope1():
        hensu_main = "aaaa"
        print(hensu_main)

    scope1()
    print(hensu_main)


if __name__ == "__main__":
    main()
