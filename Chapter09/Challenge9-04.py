import csv
movies=[["トップガン", "危険な情事", "マイノリティ.リポート"],["タイタニック","レヴェナント","インセプション"],["トレーニング.デイ","マン.オン.ファイア","フライト"]]
with open("st.csv","w")as f:
    w = csv.writer(f,delimiter=",")
    for show in movies:
        w.writerow(show)


