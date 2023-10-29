import os


def main():
    # 書き込むファイルのパス
    path = os.path.dirname(__file__) + "\writelines.csv"

    mojicode = "utf-8"

    mode = "a"

    with open(file=path, encoding=mojicode, mode=mode) as f:
        # タブは \t
        lines = ["aaa,bbb,ccc\n", "ddd,eee,fff\n", "ggg,hhh,iii\n"]
        # lines = ["aaa\tbbb\tccc\n", "ddd\teee\tfff\n", "ggg\thhh\tiii\n"]
        f.writelines(lines)


if __name__ == "__main__":
    main()
