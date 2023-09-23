import mylib1


def main():
    # 例外をハンドリングしたうえで違う例外に包んで再度例外をあげる
    ## codeを1,2,3,4と変更して動作させてみる
    code = 1

    try:
        mylib1.raise_exception(code)
    except IndexError as e:
        print("IndexErrorだけをハンドリングしたよ")
    else:
        print("例外が起こらなかったときにだけやりたいこと")
    finally:
        print("例外が起こっても起こらなくてもやりたいことを書くところ")

    print("処理が終わりました")


if __name__ == "__main__":
    main()
