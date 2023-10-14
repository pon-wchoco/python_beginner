import os
import random
import string


# ※注意
# ディスクとメモリに余裕がある人だけ！
def main():
    # 読み込むファイルのパス
    path = os.path.dirname(__file__) + "\dekai_file.txt"
    mojicode = "utf-8"

    # 2Gバイトのファイルを読み込む
    with open(file=path, encoding=mojicode) as f:
        # 全体を文字列として取得
        txt = f.read()
        print(txt)


if __name__ == "__main__":
    main()
