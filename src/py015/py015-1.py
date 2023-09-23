import mylib1


def main():
    # 例外をハンドリングしたうえで再度例外をraizeする
    ## codeを1,2,3,4と変更して動作させてみる
    code = 1

    try:
        mylib1.raise_exception(code)
    except IndexError as e:
        print("IndexErrorだけをハンドリングしたよ")
        raise e

    print("処理が終わりました")


if __name__ == "__main__":
    main()
