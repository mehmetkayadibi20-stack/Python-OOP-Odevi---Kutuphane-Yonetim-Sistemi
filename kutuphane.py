from abc import ABC, abstractmethod

class Kaynak(ABC):
    def __init__(self, baslik, kayitNo):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, yeni_baslik):
        if yeni_baslik.strip():
            self._baslik = yeni_baslik
        else:
            print("Başlık boş kalamaz.")

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, yeni_kayitNo):
        self._kayitNo = yeni_kayitNo


class Kitap(Kaynak):
    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, yeni_yazar):
        self._yazar = yeni_yazar

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, yeni_sayi):
        if int(yeni_sayi) > 0:
            self._sayfa_sayisi = yeni_sayi
        else:
            print("Sayfa sayısı sıfırdan büyük olmalı.")

    def __str__(self):
        return f"[KİTAP] ID: {self.kayitNo} | Ad: {self.baslik} | Yazar: {self.yazar} | Sayfa: {self.sayfa_sayisi}"


class Dergi(Kaynak):
    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)
        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, yeni_donem):
        self._yayin_donemi = yeni_donem

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, yeni_sayi):
        self._sayi_no = yeni_sayi

    def __str__(self):
        return f"[DERGİ] ID: {self.kayitNo} | Ad: {self.baslik} | Dönem: {self.yayin_donemi} | Sayı: {self.sayi_no}"


class Islem(ABC):
    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass


class KitapIslem(Islem):
    def __init__(self):
        self.kitap_listesi = []

    def kitap_sayisi_getir(self):
        return len(self.kitap_listesi)

    def ekle(self):
        print("\n--- Yeni Kitap Ekle ---")
        kayitNo = input("Kitabın kayıt numarasını gir: ").strip()

        for k in self.kitap_listesi:
            if k.kayitNo == kayitNo:
                print("Bu kayıt numarası zaten kullanılıyor.")
                return

        baslik = input("Kitap adı: ")
        yazar = input("Yazar adı: ")
        sayfa_sayisi = input("Sayfa sayısı: ")

        yeni_kitap = Kitap(baslik, kayitNo, yazar, sayfa_sayisi)
        self.kitap_listesi.append(yeni_kitap)
        print("Kitap eklendi.")
        print(f"Toplam kitap sayısı: {self.kitap_sayisi_getir()}")

    def listele(self):
        print("\n--- Kitap Listesi ---")

        if not self.kitap_listesi:
            print("Henüz hiç kitap eklenmemiş.")
            return
        for kitap in self.kitap_listesi:
            print(kitap)

    def sil(self):
        print("\n--- Kitap Sil ---")
        kayitNo = input("Silinecek kitabın numarasını gir: ").strip()
        for kitap in self.kitap_listesi:
            if kitap.kayitNo == kayitNo:
                self.kitap_listesi.remove(kitap)
                print(f"{kayitNo} numaralı kitap silindi.")
                return
        print("Bu numaraya ait bir kitap bulunamadı.")

    def guncelle(self):
        print("\n--- Kitap Güncelle ---")
        kayitNo = input("Güncellenecek kitabın numarasını gir: ").strip()
        for kitap in self.kitap_listesi:
            if kitap.kayitNo == kayitNo:
                print(f"Eski Bilgiler: {kitap}")
                kitap.baslik = input("Yeni ad (değiştirmeyeceksen boş bırak): ") or kitap.baslik
                kitap.yazar = input("Yeni yazar (değiştirmeyeceksen boş bırak): ") or kitap.yazar
                kitap.sayfa_sayisi = input("Yeni sayfa sayısı (değiştirmeyeceksen boş bırak): ") or kitap.sayfa_sayisi
                print("Kitap bilgileri güncellendi.")
                return
        print("Bu numaraya ait bir kitap bulunamadı.")


class DergiIslem(Islem):
    def __init__(self):
        self.dergi_listesi = []

    def dergi_sayisi_getir(self):
        return len(self.dergi_listesi)

    def ekle(self):
        print("\n--- Yeni Dergi Ekle ---")
        kayitNo = input("Derginin kayıt numarasını gir: ").strip()

        for d in self.dergi_listesi:
            if d.kayitNo == kayitNo:
                print("Bu kayıt numarası zaten kullanılıyor.")
                return

        baslik = input("Dergi adı: ")
        yayin_donemi = input("Yayın dönemi (Aylık/Haftalık vb.): ")
        sayi_no = input("Kaçıncı sayı: ")

        yeni_dergi = Dergi(baslik, kayitNo, yayin_donemi, sayi_no)
        self.dergi_listesi.append(yeni_dergi)
        print("Dergi eklendi.")
        print(f"Toplam dergi sayısı: {self.dergi_sayisi_getir()}")

    def listele(self):
        print("\n--- Dergi Listesi ---")

        if not self.dergi_listesi:
            print("Henüz hiç dergi eklenmemiş.")
            return
        for dergi in self.dergi_listesi:
            print(dergi)

    def sil(self):
        print("\n--- Dergi Sil ---")
        kayitNo = input("Silinecek derginin numarasını gir: ").strip()
        for dergi in self.dergi_listesi:
            if dergi.kayitNo == kayitNo:
                self.dergi_listesi.remove(dergi)
                print(f"{kayitNo} numaralı dergi silindi.")
                return
        print("Bu numaraya ait bir dergi bulunamadı.")

    def guncelle(self):
        print("\n--- Dergi Güncelle ---")
        kayitNo = input("Güncellenecek derginin numarasını gir: ").strip()
        for dergi in self.dergi_listesi:
            if dergi.kayitNo == kayitNo:
                print(f"Eski Bilgiler: {dergi}")
                dergi.baslik = input("Yeni ad (değiştirmeyeceksen boş bırak): ") or dergi.baslik
                dergi.yayin_donemi = input("Yeni dönem (değiştirmeyeceksen boş bırak): ") or dergi.yayin_donemi
                dergi.sayi_no = input("Yeni sayı (değiştirmeyeceksen boş bırak): ") or dergi.sayi_no
                print("Dergi bilgileri güncellendi.")
                return
        print("Bu numaraya ait bir dergi bulunamadı.")


class Menu:
    @staticmethod
    def arayuz_yazdir():
        print("\n" + "-"*30)
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Güncelle")
        print("4. Kitapları Listele")
        print("5. Dergi Ekle")
        print("6. Dergi Sil")
        print("7. Dergi Güncelle")
        print("8. Dergileri Listele")
        print("9. Çıkış")
        print("-"*30)


def ana_program():
    kitap_modulu = KitapIslem()
    dergi_modulu = DergiIslem()

    while True:
        Menu.arayuz_yazdir()
        secim = input("Ne yapmak istiyorsun? (1-9 arası seç): ").strip()

        if secim == "1":
            kitap_modulu.ekle()
        elif secim == "2":
            kitap_modulu.sil()
        elif secim == "3":
            kitap_modulu.guncelle()
        elif secim == "4":
            kitap_modulu.listele()
        elif secim == "5":
            dergi_modulu.ekle()
        elif secim == "6":
            dergi_modulu.sil()
        elif secim == "7":
            dergi_modulu.guncelle()
        elif secim == "8":
            dergi_modulu.listele()
        elif secim == "9":
            print("Programdan çıkılıyor. Görüşürüz!")
            break
        else:
            print("Geçersiz seçim. Sadece 1 ile 9 arasında bir rakam gir.")

if __name__ == "__main__":
    ana_program()