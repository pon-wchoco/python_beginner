import mylib1


def main():
    # 例外をハンドリングしたうえで絶対やりたいことをやる
    ## codeを1,2,3,4と変更して動作させてみる
    code = 1

    try:
        mylib1.raise_exception(code)
    except IndexError as e:
        print("IndexErrorだけをハンドリングしたよ")
    finally:
        print("例外が起こっても起こらなくてもやりたいことを書くところ")

    print("処理が終わりました")


if __name__ == "__main__":
    main()
