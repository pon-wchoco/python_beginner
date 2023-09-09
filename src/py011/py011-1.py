def main():
    hensu_main = "メイン変数"

    # 範囲１
    def scope1():
        hensu_scope1 = "スコープ1の変数"

        # 範囲２
        def scope2():
            hensu_scope2 = "スコープ2の変数"

            # 範囲３－１
            def scope3_1():
                hensu_scope3_1 = "スコープ3_1の変数"
                print(hensu_scope3_1)

            # 範囲３－１
            def scope3_2():
                hensu_scope3_2 = "スコープ3_2の変数"
                print(hensu_scope3_2)

            print(hensu_scope2)
            scope3_1()
            scope3_2()

        print(hensu_scope1)
        scope2()

    print(hensu_main)
    scope1()


if __name__ == "__main__":
    main()
