import os


def main():
    # 書き込むファイルのパス
    path = os.path.dirname(__file__) + "\writelines.txt"

    mojicode = "utf-8"

    mode = "a"

    with open(file=path, encoding=mojicode, mode=mode) as f:
        # 改行は \n
        lines = ["おはよう\n", "こんにちは\n", "こんばんは\n"]
        f.writelines(lines)


if __name__ == "__main__":
    main()
