import mylib1


def main():
    # 例外を具体的にハンドリングしてみる
    # except 例外クラス as e:
    code = 1

    try:
        mylib1.raise_exception(code)
    except IndexError as e:
        print("IndexErrorだけをハンドリングしたよ。詳細はこれだよ", e)

    print("処理が終わりました")


if __name__ == "__main__":
    main()
