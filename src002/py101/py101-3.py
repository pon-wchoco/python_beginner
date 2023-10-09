import os


def main():
    # 読み込むファイルのパス
    path = os.path.dirname(__file__) + "\python.txt"
    mojicode = "utf-8"

    with open(file=path, encoding=mojicode) as f:
        # 1行づつ読み込みながら処理する
        for line in f:
            print(line)


if __name__ == "__main__":
    main()
