borc = 50
while borc > 0:
    print("Amount Due:", borc)
    qepik = int(input("Insert Coin: "))
    if qepik == 25 or qepik == 10 or qepik == 5:
        borc = borc - qepik
qaytarilmali_pul = abs(borc)
print("Change Owed:", qaytarilmali_pul)
