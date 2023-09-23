import mylib1


def main():
    # 例外を具体的にハンドリングしてみる
    ## codeを1,2,3,4と変更して動作させてみる
    code = 1

    try:
        mylib1.raise_exception(code)
    except IndexError as e:
        print("IndexErrorだけをハンドリングしたよ。詳細はこれだよ", e)

    print("処理が終わりました")


if __name__ == "__main__":
    main()
