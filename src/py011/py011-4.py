def main():
    def kansu(s):
        print(s + " 実行！\n")

    # 範囲１
    def scope1():
        kansu("スコープ1")

        # 範囲２
        def scope2():
            kansu("スコープ2")

            # 範囲３－１
            def scope3_1():
                kansu("スコープ3-1")

            # 範囲３－１
            def scope3_2():
                kansu("スコープ3-2")

            scope3_1()
            scope3_2()

        scope2()

    scope1()


if __name__ == "__main__":
    main()
