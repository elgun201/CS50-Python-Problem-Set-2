nomre=input("Nomreni daxil et:")
sehv_sayi = 0
if len(nomre) < 2 or len(nomre) > 6 :
    sehv_sayi = 0
elif not ((nomre[0] >= "A" and nomre[0] <= "Z") or (nomre[0] >= "a" and nomre[0] <= "z")):
    sehv_sayi = 1
elif not ((nomre[1] >= "A" and nomre[1] <= "Z") or (nomre[1] >= "a" and nomre[1] <= "z")):
    sehv_sayi = 1
else:
    index = 2
    reqem_basladi = 0
    while index < len(nomre):
        simvol = nomre[index]
        reqemmi = 0
        if simvol >= "0" and simvol <= "9":
            reqemmi = 1
        herfmi = 0
        if (simvol >= "A" and simvol <= "Z") or (simvol >= "a" and simvol <= "z"):
            herfmi = 1
        if reqemmi == 0 and herfmi == 0:
            sehv_sayi = 1
            break
        if reqemmi == 1:
            if reqem_basladi == 0:
                if simvol == "0":
                    sehv_sayi = 1
                    break
                reqem_basladi = 1
        else:
            if reqem_basladi == 1:
                sehv_sayi = 1
                break
        index = index + 1
if sehv_sayi == 0:
    print("Valid")
else:
    print("Invalid")
