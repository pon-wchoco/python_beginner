import mylib1


def main():
    ## codeを1,2,3と変更して動作させてみる
    code = 1
    mylib1.raise_exception(code)
    print("処理が終わりました")


if __name__ == "__main__":
    main()
