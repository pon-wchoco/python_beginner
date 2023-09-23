import mylib1


def main():
    # 例外をハンドリングしたうえで違う例外に包んで再度例外をあげる
    code = 1

    try:
        mylib1.raise_exception(code)
    except IndexError as e:
        print("IndexErrorだけをハンドリングしたよ")
        raise ValueError(e)

    print("処理が終わりました")


if __name__ == "__main__":
    main()
