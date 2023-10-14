import os
import random
import string


# ※注意
# ディスクとメモリに余裕がある人だけ！
def main():
    # 読み込むファイルのパス
    path = os.path.dirname(__file__) + "\dekai_file.txt"
    mojicode = "utf-8"

    # でかいファイルを1行読み込む
    with open(file=path, encoding=mojicode) as f:
        # 1行づつ読み込みながら処理する
        for line in f:
            print(line)


if __name__ == "__main__":
    main()
