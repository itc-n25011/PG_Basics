me = {"height": "173cm",
     "color": "green",
     "writer": "鳥山明"}
n = input("好きな作家を入力してください")
if n in me:
    me = me[n]
    print(me)
else:
    print("わかりました")






