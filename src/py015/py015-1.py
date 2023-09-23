import mylib1


def main():
    # 例外をハンドリングしたうえで再度例外を発生させる
    code = 1

    try:
        mylib1.raise_exception(code)
    except IndexError as e:
        print("IndexErrorだけをハンドリングしたよ")
        raise e

    print("処理が終わりました")


if __name__ == "__main__":
    main()
