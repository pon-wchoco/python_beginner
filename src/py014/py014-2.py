import mylib1


def main():
    # 例外を雑にハンドリングしてみる
    ## codeを1,2,3,4と変更して動作させてみる
    code = 1

    try:
        mylib1.raise_exception(code)
    except:
        print("例外ハンドリングしたよ")

    print("処理が終わりました")


if __name__ == "__main__":
    main()
