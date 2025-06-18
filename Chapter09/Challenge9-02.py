a = input("あなたの好きな食べ物?")
with open("food.txt","w") as f:
    f.write(a)

