import mylib1


def main():
    ## codeを0, 1,2,3と変更して動作させてみる
    code = 0
    mylib1.raise_exception(code)
    print("処理が終わりました")


if __name__ == "__main__":
    main()
