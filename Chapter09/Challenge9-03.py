import csv
movies=[["Top Gun", "Risky BUsiness", "Minority Report"],["Titanic","The Revent","Inception"],["Traning Day","man on Fire","Flight"]]
with open("st.csv","w")as f:
    w = csv.writer(f,delimiter=",")
    for show in movies:
        w.writerow(show)


