#BİLGİSAYAR PROGRAMLAMA 2 ÖDEV: 3 - CLASS
def main():
    magaza = ""
    while True:
        magaza_adi = input("Magaza adi giriniz (cikmak icin '-1' girin): ")
        print()
        if magaza_adi == "-1":
            break
        satici_adi = input("Satici adi giriniz: ")
        satici_cinsi = input("Satici cinsi giriniz: ")
        satis_tutari = float(input("Satis tutarini giriniz: "))

        magaza = Magaza(magaza_adi, satici_adi, satici_cinsi)
        i = f"{magaza_adi}-{satici_adi}"
        magaza.magazalar[i]["satis_tutari"] += satis_tutari
