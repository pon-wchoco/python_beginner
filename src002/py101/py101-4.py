import os
import random
import string


# ※注意
# ディスクとメモリに余裕がある人だけ！
def main():
    # 読み込むファイルのパス
    path = os.path.dirname(__file__) + "\dekai_file.txt"
    mojicode = "utf-8"

    # 2Gバイトのファイルを作る
    create_large_text_file(path, 2)


def create_large_text_file(file_path, file_size_gb):
    file_size_bytes = file_size_gb * (1024**3)  # ギガバイトをバイトに変換
    line_size = 80  # 1行の文字数
    chunk_size = 128 * 1024  # 100キロバイトずつ書き込む

    j = 0
    with open(file_path, "w") as file:
        while os.path.getsize(file_path) < file_size_bytes:
            # ランダムなテキストデータを生成
            random_text = "".join(random.choices(string.ascii_letters, k=chunk_size))
            # テキストデータを1行ずつ書き込み、改行コードを挿入
            for i in range(0, len(random_text), line_size):
                line = random_text[i : i + line_size]
                file.write(line + "\n")
            j = j + 1
            print("ファイル生成:" + str(j / 10000) + "ギガバイト")


if __name__ == "__main__":
    main()
