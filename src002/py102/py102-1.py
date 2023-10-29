import os


def main():
    # 書き込むファイルのパス
    path = os.path.dirname(__file__) + "\write.txt"

    # mojicode = "utf-8"
    mojicode = "shift_jis"

    # "a" : 追記モード
    # "w" : 上書きモード
    # "x" : 存在しなかったら作成するモード
    mode = "a"  # "a", "w", "x"

    with open(file=path, encoding=mojicode, mode=mode) as f:
        # 改行は \n
        f.write("こんにちは")


if __name__ == "__main__":
    main()
