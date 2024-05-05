class Banka:
    def __init__(self,isim):
        self.isim = isim
        self.hesaplar= {}
    def hesap_olustur(self, hesap_no,isim,bakiye):
        if hesap_no not in self.hesaplar:
            self.hesaplar[hesap_no] = {'isim':isim,'bakiye':bakiye}
            print(f"{isim} adli musteri icin {hesap_no} numarali hesap olusturldu")
        else:
            print("Bu hesap numarsi zaten kullanimda.")
    def bakiye_sorgula(self,hesap_no):
        if hesap_no in self.hesaplar:
            return self.hesaplar[hesap_no]['bakiye']
        else:
            print("Hesap bulunamadi.")
            return None 
    def para_yatir(self,hesap_no,miktar):
        if hesap_no in self.hesaplar:
            self.hesaplar[hesap_no]['bakiye'] += miktar
            print(f"{hesap_no} numarali hesaba {miktar} TL yatirildi")
        else:
            print("Hesap bulunamdi") 
    def para_cek(self,hesap_no, miktar):
        if hesap_no in self.hesaplar:
            if self.hesaplar[hesap_no]['bakiye'] >= miktar:
                self.hesaplar[hesap_no]['bakiye'] -= miktar
                print(f"{hesap_no} numarali hesaptan {miktar} TL cekildi.")
            else:
                print("Yetersiz bakiye")
        else:
            print("Hesap bulunamadi.")

banka = Banka("Ziraat Bankası")
banka.hesap_olustur("123456", "ilhan Koca", 1000)
print("Hesap Bakiyesi:", banka.bakiye_sorgula("123456"))
banka.para_yatir("123456", 500)
print("Hesap Bakiyesi:", banka.bakiye_sorgula("123456"))
banka.para_cek("123456", 200)
print("Hesap Bakiyesi:", banka.bakiye_sorgula("123456"))
