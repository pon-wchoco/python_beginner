# ライブラリ１のモジュール１
def raise_exception(i):
    code = int(i)
    if code == 1:
        ## よくあるエラーが発生するパターン
        ## 配列に存在しない要素番号をつかってしまった
        l = [1, 2, 3]
        l[100]

    if code == 2:
        ## ゼロで割り算してしまった
        1 / 0

    if code == 3:
        ## 自分で例外を発生させてみる
        print("これから自分で例外を発生させるよ")

        raise OriginalException("自分で例外発生させて、自分でメッセージを設定できるよ")

    if code == 4:
        print("正常終了")
        return

    raise Exception("引数に指定した番号がおかしいです。1-3の数字を指定して下さい。")


class OriginalException(Exception):
    # 独自の例外クラスの定義
    ...
