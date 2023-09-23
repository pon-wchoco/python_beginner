import mylib1


def main():
    # 例外を雑にハンドリングしてみる
    # try: except:
    code = 1

    try:
        mylib1.raise_exception(code)
    except:
        print("例外ハンドリングしたよ")

    print("処理が終わりました")


if __name__ == "__main__":
    main()
