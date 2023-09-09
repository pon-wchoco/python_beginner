def main():
    hensu_main = "メイン変数"

    # 範囲１
    def scope1():
        # メイン変数が使える
        print("スコープ1開始")
        print(hensu_main)
        hensu_scope1 = "スコープ1の変数"

        # 範囲２
        def scope2():
            # メイン変数もスコープ１の変数も使える
            print("\nスコープ2開始")
            print(hensu_main)
            print(hensu_scope1)
            hensu_scope2 = "スコープ2の変数"

            # 範囲３－１
            def scope3_1():
                # メイン変数もスコープ１の変数もスコープ２の変数も使える
                print("\nスコープ3_1開始")
                print(hensu_main)
                print(hensu_scope1)
                print(hensu_scope2)
                hensu_scope3_1 = "スコープ3_1の変数"
                print(hensu_scope3_1)

            # 範囲３－１
            def scope3_2():
                # メイン変数もスコープ１の変数もスコープ２の変数も使える
                print("\nスコープ3_2開始")
                print(hensu_main)
                print(hensu_scope1)
                print(hensu_scope2)
                hensu_scope3_2 = "スコープ3_2の変数"
                print(hensu_scope3_2)
                # hensu3_1は使えない
                # print(hensu_scope3_1)

            print(hensu_scope2)
            scope3_1()
            scope3_2()

        print(hensu_scope1)
        scope2()

    print(hensu_main)
    scope1()


if __name__ == "__main__":
    main()
