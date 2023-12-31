# ライブラリ１のモジュール１
def raise_exception(i):
    # 引数はint型だけを期待している
    code = int(i)

    if code == 0:
        print("正常終了！！")
        return

    if code == 1:
        ## よくあるエラーが発生するパターン
        ## 配列に存在しない要素番号をつかってしまった
        l = [1, 2, 3]
        l[100]

    if code == 2:
        ## ゼロで割り算してしまった
        1 / 0

    raise ValueError("引数に指定した番号がおかしいです。1-2の数字を指定して下さい。")
