import mylib1


def main():
    # 例外をちょっと良くハンドリングしてみる
    # except 例外クラス:
    code = 1

    try:
        mylib1.raise_exception(code)
    except IndexError:
        print("IndexErrorだけをハンドリングしたよ")

    print("処理が終わりました")


if __name__ == "__main__":
    main()
