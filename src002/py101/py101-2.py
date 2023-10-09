import os


def main():
    # 読み込むファイルのパス
    path = os.path.dirname(__file__) + "\python.txt"
    mojicode = "utf-8"

    with open(file=path, encoding=mojicode) as f:
        # 全体を1行づつのリストとして取得
        lines = f.readlines()

    # リストオブジェクトを表示してみる
    print(lines)

    print("-----------")
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
