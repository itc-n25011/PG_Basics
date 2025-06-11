qs = [1,2,3,4,5]
while True:
    a = input("数字で入力するか、qで終了します")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("数字を入力するか、qで終了します。")
    if a in qs:
        print("正解")
    else:
        print("不正解")


