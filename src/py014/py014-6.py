import mylib1


def main():
    # 例外のハンドリングの順番を確認してみる
    code = 1

    try:
        mylib1.raise_exception(code)
    except Exception as e:
        print("Exceptionをハンドリングしたよ。詳細はこれだよ", e)
    except IndexError as e:
        print("IndexErrorをハンドリングしたよ。詳細はこれだよ", e)
    except ZeroDivisionError as e:
        print("ZeroDivisionErrorをハンドリングしたよ。詳細はこれだよ", e)

    print("処理が終わりました")


if __name__ == "__main__":
    main()
