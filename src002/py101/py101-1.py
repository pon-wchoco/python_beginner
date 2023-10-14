import os


def main():
    # 読み込むファイルのパス
    path = os.path.dirname(__file__) + "\python.txt"
    # path = os.path.dirname(__file__) + "\python_shift_jis.txt"

    mojicode = "utf-8"
    # mojicode = "shift_jis"

    with open(file=path, encoding=mojicode) as f:
        # 全体を文字列として取得
        txt = f.read()
        print(txt)


if __name__ == "__main__":
    main()
