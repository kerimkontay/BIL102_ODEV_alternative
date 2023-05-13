#BİLGİSAYAR PROGRAMLAMA 2 ÖDEV: 3 - CLASS

class Magaza:
    magazalar = {}
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        # data attributes, private
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satis_tutari = 0
        self.__kaydet()
        
    def __kaydet(self):
        i = f"{self.__magaza_adi}-{self.__satici_adi}"
        value = {"magaza_adi": self.__magaza_adi,
                 "satici_adi": self.__satici_adi,
                 "satici_cinsi": self.__satici_cinsi,
                 "satis_tutari": self.__satis_tutari}
        self.magazalar[i] = value

    def magazaSatisTutar(self, magaza_adi, satici_adi):
        i = f"{magaza_adi}-{satici_adi}"
        if i in self.magazalar:
            return self.magazalar[i]["satis_tutari"]
        else:
            return None

    def __str__(self):
        result = ""
        for i in self.magazalar:
            magaza_adi = self.magazalar[i]["magaza_adi"]
            satici_adi = self.magazalar[i]["satici_adi"]
            satis_tutari = self.magazalar[i]["satis_tutari"]
            result += f"{magaza_adi} - {satici_adi}: {satis_tutari:,.2f}\n"
        return result


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
