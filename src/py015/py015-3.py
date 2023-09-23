import mylib1


def main():
    # 自分の例外型(クラス)を作ってみる
    code = 3

    try:
        mylib1.raise_exception(code)
    except mylib1.OriginalException as e:
        print("自作の例外クラスだけをハンドリングしたよ")
        raise e

    print("処理が終わりました")


if __name__ == "__main__":
    main()
