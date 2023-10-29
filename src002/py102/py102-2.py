import os


def main():
    # 書き込むファイルのパス
    path = os.path.dirname(__file__) + "\writelines.txt"

    mojicode = "utf-8"
    # mojicode = "shift_jis"

    # "a" : 追記モード
    # "w" : 上書きモード
    # "x" : 存在しなかったら作成するモード
    # "r" : 読み込みモード（modeを省略すると"r"が指定されたことになる！）
    mode = "a"  # "a", "w", "x", "r"

    with open(file=path, encoding=mojicode, mode=mode) as f:
        # 改行は \n
        lines = ["おはよう\n", "こんにちは\n", "こんばんは\n"]
        f.writelines(lines)


if __name__ == "__main__":
    main()
