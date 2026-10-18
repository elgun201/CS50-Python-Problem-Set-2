text=input("Metni daxil et:")
a=["a","e","i","o","u"]
yeni_metn=""
for i in text:
    if a.count(i)==0:
        yeni_metn=yeni_metn+i
print(yeni_metn)
        
    
