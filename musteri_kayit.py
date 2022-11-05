import tkinter as tk
from PIL import ImageTk, Image
from datetime import datetime, timedelta
import csv
import sys

kullanici_ismi = '123'
sifre_ismi = '123'
filename = 'ornek_resim_test.jpg' 

# 			~~~Deneysel~~~
# Programda kullanmak icin .py dosyamizin oldugu dizinde bir 'ornek_resim_test.jpg' adinda
# bir resim bulunmalidir. 
# Resmi direkt olarak .py dosyamiza eklemek istersek Asagidaki kod,
# resimstring`den .jpg`ye base64decode ederek otomatik olarak resmi meydana getirecektir.

'''
import base64
resimstring = b'...........'    # base64 formatina encode edilmis resim buraya yaziniz
imgdata = base64.b64decode(resimstring)
with open(filename, 'wb') as f:
    f.write(imgdata)
'''

try:
    filename150 = 'ornek_resim_test150.jpg' 
    filename300 = 'ornek_resim_test300.jpg'
    img150 = Image.open(filename) 
    img150 = img150.resize((150, 150)) 
    img150.save(filename150)  

    img300 = Image.open(filename) 
    img300 = img300.resize((300, 300)) 
    img300.save(filename300)  

except FileNotFoundError as error:
    print(error)
    print(".py`nin oldugu dizinde 'ornek_resim_test.jpg' isminde dosya olmalidir")
    sys.exit()


class Musteri():    
    musteriler = []
    
    def __init__(self, isim, soyad, tcno, araba):
        self.isim = isim
        self.soyad = soyad
        self.tcno = tcno                
        self.araba = araba
        self.musterilere_ekle()
        
    def __str__(self):
        return 'isim: {} soyad: {} tcno: {} kiraladigi araba ===>> {}'.format(self.isim, self.soyad, self.tcno, self.araba)
    
    def musterilere_ekle(self):
        self.musteriler.append(self.isim)
    
    
class Araba():    
    arabalar = []
    
    def __init__(self, marka = None, yil = None, plaka = None, fiyat = None, durum = 'bos'):
        self.marka = marka
        self.yil = yil
        self.fiyat = fiyat
        self.plaka = plaka 
        self.durum = durum 
        self.gun = 0
    
        if marka == None:
            self.yeni_araba_bilgisi_gir()
        self.arabalara_ekle()
    
    def __str__(self):
        mm = 'marka: {} yil: {} plaka: {} gunluk fiyat: {} durum: {}'
        return mm.format(self.marka, self.yil, self.plaka, self.fiyat, self.durum)
    
    def yeni_araba_bilgisi_gir(self):
        self.marka = input("arabanin markasini giriniz : ")
        self.yil = input("arabanin yilini giriniz : ")
        self.fiyat = input("arabanin fiyatini giriniz : ")
        self.plaka = input("arabanin plakasini giriniz : ")
        
    def arabalara_ekle(self):
        self.arabalar.append(self.marka)

M = {1:'m1',
     2:'m2',
     3:'m3',   # Musteri sinifi icin sozluk
     4:'m4',   # nesne tanimlarken kendisi buraya baksin 
     5:'m5',   # degerler icinde string arasin
     6:'m6',   # ilk buldugun stringin yerine nesneyi yapistir
     7:'m7',
     8:'m8',
     9:'m9'}    
  
A = {1:'a1',
     2:'a2',  # Araba sinifi icin sozluk
     3:'a3',
     4:'a4',
     5:'a5',
     6:'a6',
     7:'a7',
     8:'a8',
     9:'a9'} 

A[1] = Araba('mercedes', '2002', '34 QQ 358', '1000')  # ontanimli arabalar
A[2] = Araba('opel', '2010', '34 QQ 668', '700') 
A[3] = Araba('ford', '1995', '06 QQ 107', '500')


class AnaEkran(tk.Tk):
    def giris(self):
        if self.entry1.get() == kullanici_ismi and self.entry2.get() == sifre_ismi:
            self.etiket4['text'] = "hos geldiniz"
            self.destroy()
          
        else:
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')
            self.etiket4['text'] = 'kullanici ismi veya sifre gecersiz'
    
    def patlat(self):
        self.destroy()
        sys.exit()
        
    
    def __init__(self):
        super().__init__()
        
        self.geometry('430x400+400+150')
        self.title("giris")
        self.protocol('WM_DELETE_WINDOW', lambda: self.patlat())
        self.img = ImageTk.PhotoImage(Image.open(filename150))
        self.image = tk.Label(self, image = self.img)
        self.image.place(x = 220, y = 0) 
        
        self.etiket1 = tk.Label(self, text = "kullanici ismi", font = ('Liberation Serif', 12))
        self.etiket2 = tk.Label(self, text = 'kullanici sifresi', font = ('Liberation Serif', 12))
        self.etiket3 = tk.Label(self, text = "Giris", font = ('Liberation Serif', 20))
        self.etiket4 = tk.Label(self, font = ('Liberation Serif', 11), fg = 'red3')
        
        self.entry1 = tk.Entry(self, borderwidth = 2, width = 27, font = ('Liberation Serif', 17))
        self.entry2 = tk.Entry(self, borderwidth = 2, width = 27, show = '*', font = ('Liberation Serif', 17))
        
        self.buton = tk.Button(self, text = "Giris", padx = 135, pady = 10, bg = 'DeepSkyBlue2', command = lambda: self.giris())
        
        self.buton.place(x = 67, y = 330)
        self.etiket1.place(x = 67, y = 170)
        self.etiket2.place(x = 67, y = 240) 
        self.etiket3.place(x = 67, y = 30)
        self.etiket4.place(x = 15, y = 70)
        self.entry1.place(x = 67, y = 195)
        self.entry2.place(x = 67, y = 265)


class YeniPencere(tk.Tk):              
    def araba_ekle_sil(self, islem):
        
        if islem == 'ekle':
            self.show_frame(ArabaEkle)
        elif islem == 'duzenle':
            self.show_frame(ArabaDuzenle)
            goster(self.frames[ArabaDuzenle], A, Araba)
        elif islem == 'sil':
            self.show_frame(ArabaSil)
            goster(self.frames[ArabaSil], A, Araba)
        else:
            quit()
        
    def musteri_ekle(self):
        self.show_frame(MusteriEkle)
        goster(yenipencere.frames[MusteriEkle], A, Araba)
        return
            
    def musteri_bilgisi_duzenle(self):
        self.show_frame(MusteriDuzenle)  
        goster(yenipencere.frames[MusteriDuzenle], M, Musteri)
        goster(yenipencere.frames[MusteriDuzenle], A, Araba, yenipencere.frames[MusteriDuzenle].text2)
        return

    def musteri_sil(self):
        self.show_frame(MusteriSil)
        goster(yenipencere.frames[MusteriSil], M, Musteri)
        return
            
    def logu_goruntule(self):
        self.frames[LoguGoruntule].text.delete('1.0', 'end')
        for val in A.values():
            if isinstance(val, Araba):
                self.frames[LoguGoruntule].text.insert(tk.INSERT, "{}  {} --->> {} gun kiralanmistir\n".format(val.marka, val.yil, val.gun))
        self.frames[LoguGoruntule].text.insert(tk.INSERT, "\n {}.{}.{} tarihindeki toplam gelirimiz = {}".format(self.tarih.day, self.tarih.month, self.tarih.year, self.toplam_gelir))
        
        self.show_frame(LoguGoruntule)
        return
            
    def csv_olarak_aktar(self):
                
        with open("musteri.csv", "w", newline='') as mcsv: 
            thewriter = csv.writer(mcsv)                        
            thewriter.writerow(["isim", 'tcno', 'arabasi', 'gunluk ucret'])
            for val in M.values():
                if isinstance(val, Musteri):
                    thewriter.writerow([val.isim, val.tcno, val.araba.marka, val.araba.fiyat])
        
        with open("araba.csv", 'w', newline='') as acsv:
            thewriter = csv.writer(acsv)
            thewriter.writerow(["marka", 'yil', 'plaka', 'ucret', 'durum', 'gun sayisi'])
            for val in A.values():
                if isinstance(val, Araba):
                    thewriter.writerow([val.marka, val.yil, val.plaka, val.fiyat, val.durum, val.gun])
        self.frames[StartPage].etiket['text'] = 'bilgiler musteri.csv ve araba.csv ye aktarildi'
        self.show_frame(StartPage)
        return
    
    
    def gunu_bitir(self):
        for val in M.values():
            if isinstance(val, Musteri):
                if val.araba.durum == 'dolu':
                    val.araba.gun +=1
        self.toplam_gelir = self.toplam_gelir_hesapla()
        self.tarih += timedelta(days=1)
        self.frames[StartPage].etiket['text'] = 'gun bitti. Bu gunun tarihi ---> {}.{}.{}'.format(self.tarih.day, self.tarih.month, self.tarih.year)
        self.sayac += 1
        self.show_frame(StartPage)
        return  

    def toplam_gelir_hesapla(self):
        for val in A.values():
            if isinstance(val, Araba):
                if val.durum == 'dolu':
                    self.toplam_gelir += int(val.fiyat)
        return self.toplam_gelir
        
    
    def tum_kayitlari_goster(self):
        self.show_frame(TumKayitlariGoster)
        goster(yenipencere.frames[TumKayitlariGoster], M, Musteri , yenipencere.frames[TumKayitlariGoster].text1)
        goster(yenipencere.frames[TumKayitlariGoster], A, Araba , yenipencere.frames[TumKayitlariGoster].text2)
        return
    
    def sorgula(self):
        self.show_frame(Sorgula)
        return
    
                
    def __init__(self):
        super().__init__()
        self.toplam_gelir = 0
        self.sayac = 1
        self.tarih = datetime.today()
        self.title('menu')
        self.geometry('700x500+300+150')
        self.resizable(width=False, height=False)

        
        self.container = tk.Frame(self)
        self.container.grid(padx = 500, pady = 500)
  
        self.menubar = tk.Menu(self)  # menu
        
        self.menu_islem1 = tk.Menu(self.menubar, tearoff = 0)
        self.menu_islem1.add_command(label = 'musteri ekle', command = lambda: self.musteri_ekle())
        self.menu_islem1.add_command(label = 'musteri bilgisi duzenle', command = lambda: self.musteri_bilgisi_duzenle())
        self.menu_islem1.add_command(label = 'musteri sil', command = lambda: self.musteri_sil())
        self.menubar.add_cascade(label = 'MUSTERI', menu = self.menu_islem1, background = 'khaki3')
        
        self.menu_islem2 = tk.Menu(self.menubar, tearoff = 0)
        self.menu_islem2.add_command(label = 'araba ekle', command = lambda: self.araba_ekle_sil('ekle'))
        self.menu_islem2.add_command(label = 'araba bilgisi duzenle', command =  lambda: self.araba_ekle_sil('duzenle'))
        self.menu_islem2.add_command(label = 'araba sil', command = lambda: self.araba_ekle_sil('sil'))
        self.menubar.add_cascade(label = 'ARABA', menu = self.menu_islem2, background = 'khaki3')
        
        self.menu_islem3 = tk.Menu(self.menubar, tearoff = 0)
        self.menu_islem3.add_command(label = 'tum araba ve musterileri goster', command = lambda: self.tum_kayitlari_goster())
        self.menu_islem3.add_command(label = 'sorgula', command = lambda: self.sorgula())       
        self.menubar.add_cascade(label = "GENEL", menu = self.menu_islem3, background = 'khaki3')
        
        self.menu_islem4 = tk.Menu(self.menubar, tearoff = 0)
        self.menu_islem4.add_command(label = 'gunu bitir', command = lambda: self.gunu_bitir())
        self.menu_islem4.add_command(label = 'logu goruntule', command = lambda: self.logu_goruntule())
        self.menu_islem4.add_command(label = 'CSV olarak aktar', command = lambda: self.csv_olarak_aktar())
        self.menubar.add_cascade(label = 'DIGER ISLEMLER', menu = self.menu_islem4, background = 'khaki3')
        
        self.config(menu = self.menubar)

        self.frames = {}
        
        for F in (StartPage, MusteriEkle, MusteriSil, ArabaEkle, ArabaSil, MusteriDuzenle, ArabaDuzenle, TumKayitlariGoster, Sorgula, LoguGoruntule):
            
            frame = F(self)
            self.frames[F] = frame
            frame.grid(column = 0, row = 0,sticky = 'nsew')
            
            
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        self.frames[cont].tkraise()
        
        

class StartPage(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.tarih_ilk = datetime.today()
        self.etiket = tk.Label(self, text = 'Menuden Islem Seciniz. Bu gunun tarihi ---> {}.{}.{}'.format(self.tarih_ilk.day, self.tarih_ilk.month, self.tarih_ilk.year))
        self.etiket.place(x = 170, y = 400)
        self.img = ImageTk.PhotoImage(Image.open(filename300))
        self.image = tk.Label(self, image = self.img)
        self.image.place(x = 200, y = 0) 
        
        
class MusteriSil(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        
        self.entry = tk.Entry(self)
        self.buton = tk.Button(self, text = 'musteriyi sil', command = lambda: self.musteri_sil())
        self.text = tk.Text(self, height = 15, width = 50)
        self.etiket = tk.Label(self, text = "silinecek musterinin no'su")
        self.etiket2 = tk.Label(self, text = 'musteriler')
        self.etiket3 = tk.Label(self)
        
        self.buton.place(x = 350, y = 400)
        self.text.place(x = 10, y = 30)
        self.entry.place(x = 10, y = 400)
        self.etiket.place(x = 10, y = 380)
        self.etiket2.place(x = 10, y = 10)
        self.etiket3.place(x = 350, y = 370)
        
    def musteri_sil(self):
        if self.entry.get().isnumeric() == False:
            self.etiket3['text'] = 'yanlis deger girildi'
            return
        musteri_no = int(self.entry.get())
        if boyle_biri_var_mi(musteri_no, M) == 'yok': 
            self.etiket3['text'] = 'boyle biri yok'
            return
        self.etiket3['text'] = ''
        M[musteri_no].araba.durum = 'bos'
        M[musteri_no] = "m{}".format(str(musteri_no)) 
        self.etiket3['text'] = 'musteri silindi'
        goster(yenipencere.frames[MusteriSil], M, Musteri)
        
class MusteriEkle(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        
        self.etiket = tk.Label(self, text = "yeni musteri islemleri" )
        self.etiket1 = tk.Label(self, text = 'musterinin ismi')
        self.etiket2 = tk.Label(self, text = 'musterinin soyismi')
        self.etiket3 = tk.Label(self, text = 'musterinin tcno')
        self.etiket4 = tk.Label(self, text = "kiralayacagi araba no'su")
        self.etiket5 = tk.Label(self, text = 'arabalar')
        self.etiket6 = tk.Label(self)
        
        self.etiket.place(x = 250, y = 10)
        self.etiket1.place(x = 50, y = 100)
        self.etiket2.place(x = 50, y = 200)
        self.etiket3.place(x = 50, y = 300)
        self.etiket4.place(x = 50, y = 400)
        self.etiket5.place(x = 400, y = 80)  
        self.etiket6.place(x = 450, y = 375)
        
        self.entry1 = tk.Entry(self)
        self.entry2 = tk.Entry(self)
        self.entry3 = tk.Entry(self)
        self.entry4 = tk.Entry(self)
        
        self.entry1.place(x = 50, y = 120)
        self.entry2.place(x = 50, y = 220)
        self.entry3.place(x = 50, y = 320)
        self.entry4.place(x = 50, y = 420)
       
        self.buton = tk.Button(self, text = 'musteriyi ekle', command = lambda: self.musteri_ekle_fonksiyonu())
        self.buton.place(x = 500, y = 400)
                      
        self.text = tk.Text(self, height = 15, width = 55)  # burayi men deyisebilmeyim oto olsun yeni arabalarda
        self.text.place(x = 240, y = 100)
    
    def temizle(self):
        for i in (self.entry1, self.entry2, self.entry3, self.entry4):
            i.delete(0, 'end')
    

    def musteri_ekle_fonksiyonu(self):
        if entryler_dolu_mu(yenipencere.frames[MusteriEkle]) == 'doludegil':
            self.etiket6['text'] = 'lutfen bilgileri tam giriniz'
            return
        self.etiket6['text'] = ''
        if self.entry1.get().isalpha() == False:
            self.etiket6['text'] =  "soyisim formati yanlis"
            return
        if self.entry2.get().isalpha() == False:
            self.etiket6['text'] =  "soyisim formati yanlis"
            return        
        if self.entry3.get().isnumeric() == False or len(self.entry3.get()) != 11:
            self.etiket6['text'] =  "TCno format yanlis"
            return
        if self.entry4.get().isnumeric() == False:
            self.etiket6['text'] = "araba no'ya yanlis deger girildi"
            return
        if boyle_biri_var_mi(int(self.entry4.get()), A) == 'yok':
            self.etiket6['text'] = "boyle araba yok"
            return
        for val in A.values():
            if isinstance(val, Araba):
                if A[int(self.entry4.get())].durum != 'bos':
                    self.etiket6['text'] =  "bu araba zaten kullanilmakta"
                    return

        for key, val in M.items():
            if not isinstance(val, Musteri):
                sayac = key
                break

        M[sayac] = Musteri(self.entry1.get(), self.entry2.get(), self.entry3.get(), A[int(self.entry4.get())])
        A[int(self.entry4.get())].durum = 'dolu'
        goster(yenipencere.frames[MusteriEkle], A, Araba)
        self.etiket6['text'] = 'musteri eklendi'
        self.temizle()
            
        
class ArabaEkle(MusteriEkle):
    def __init__(self, *args):
        super().__init__(*args)
        self.etiket['text'] = 'yeni araba bilgileri'
        self.etiket1['text'] = 'araba markasi'
        self.etiket2['text'] = 'arabanin yili'
        self.etiket3['text'] = 'arabanin plakasi'
        self.etiket4['text'] = 'arabanin gunluk fiyati'
        self.buton['text'] = 'araba ekle'
        self.buton['command'] = lambda: self.araba_ekle_fonksiyonu()
        self.etiket5.destroy()
        self.text.destroy()
    
    def araba_ekle_fonksiyonu(self):
        if entryler_dolu_mu(yenipencere.frames[ArabaEkle]) == 'doludegil':
            self.etiket6['text'] = 'lutfen bilgileri tam giriniz'
            return
        self.etiket6['text'] = ''
        for key, val in A.items():
            if not isinstance(val, Araba):  
                sayac = key
                break
        if self.entry4.get().isnumeric() == False:
            self.etiket6['text'] = "arabanin fiyati sadece sayi olmali"
            return
        A[sayac] = Araba(self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get())
        self.etiket6['text'] = 'araba eklendi'
        self.temizle()

    
class ArabaSil(MusteriSil):
    def __init__(self, *args):        
        super().__init__(*args)
      
        self.buton['text'] = 'arabayi sil'
        self.buton['command'] = lambda: self.araba_sil()
        self.etiket3.place(x = 330, y = 360)
        self.etiket['text'] = "silinecek araba no'su"
        self.etiket2['text'] = 'arabalar'
        self.text['width'] = 84
 
    def araba_sil(self):
        if self.entry.get().isnumeric() == False:
            self.etiket3['text'] = 'yanlis deger girildi'
            return
        araba_no = int(self.entry.get())
        if boyle_biri_var_mi(araba_no, A) == 'yok': 
            self.etiket3['text'] = 'boyle araba yok'
            return
        self.etiket3['text'] = ''
        for val in A.values():
            if isinstance(val, Araba):
                if A[araba_no].durum == 'dolu': 
                    self.etiket3['text'] = 'dolu arabayi silemezsiniz ilk once \nya musteriyi sil ya da musterinin arabasini degis'
                    return
        self.etiket3['text'] = 'araba silindi'
        A[araba_no] = "m{}".format(str(araba_no))     
        goster(yenipencere.frames[ArabaSil], A, Araba)
                
class TumKayitlariGoster(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.text1 = tk.Text(self, width = 87, height = 14)
        self.text2 = tk.Text(self, width = 87, height = 14)
        self.text1.place(x = 0, y = 0)
        self.text2.place(x = 0, y = 250)
        

class Sorgula(tk.Frame): 
    def __init__(self, controller):
        super().__init__()
        self.entry = tk.Entry(self)
        self.etiket = tk.Label(self, text = 'buraya anahtar kelime gir')
        self.text = tk.Text(self, width = 60, height = 15)
        self.buton = tk.Button(self, text = 'ara', command = lambda: self.ara())
        
        self.entry.place(x = 10, y = 35)
        self.etiket.place(x = 10, y = 10)
        self.text.place(x = 150, y = 100)
        self.buton.place(x = 480, y = 430)
    
    def ara(self):
        self.text.delete(1.0, 'end')
        self.sorgulama_fonksiyonu(A, Araba)
        self.sorgulama_fonksiyonu(M, Musteri)
            
    def sorgulama_fonksiyonu(self, sozluk, sinif):
        sayac = 0
        for key, val in sozluk.items():
            if isinstance(val, sinif):
                for x in val.__dict__.values():
                    if x == self.entry.get():
                        self.text.insert(tk.INSERT, '{}\n'.format(str(key)+'.'+str(val)))
                        sayac = 1
                        break
        if sayac == 0:
            if sinif == Araba:
                kelime = "Araba"
            else:
                kelime = "Musteri"
            self.text.insert(tk.INSERT, "{}'lerin bilgilerinde bir sey bulunamadi\n\n".format(kelime))
        
        
class LoguGoruntule(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.text = tk.Text(self, width = 84 , height = 28)
        self.text.place(x = 12, y = 10)
        

class MusteriDuzenle(tk.Frame):
    def __init__(self, controller):
        super().__init__()

        self.etiket = tk.Label(self, text = "musteri bilgisi degisme" )
        self.etiket1 = tk.Label(self, text = 'musterinin ismi')
        self.etiket2 = tk.Label(self, text = 'musterinin soyismi')
        self.etiket3 = tk.Label(self, text = 'musterinin tcno')
        self.etiket4 = tk.Label(self, text = "kiralayacagi araba no'su")
        self.etiket5 = tk.Label(self, text = 'musteriler')
        self.etiket6 = tk.Label(self, text = 'arabalar')
        self.etiket7 = tk.Label(self, text = "musteri no'sunu bura gir -->")
        self.etiket8 = tk.Label(self)
        self.etiket.place(x = 250, y = 10)
        self.etiket1.place(x = 20, y = 100)
        self.etiket2.place(x = 20, y = 200)
        self.etiket3.place(x = 20, y = 300)
        self.etiket4.place(x = 20, y = 400)
        self.etiket5.place(x = 450, y = 80) 
        self.etiket6.place(x = 200, y = 80)
        self.etiket7.place(x = 210, y = 400)
        self.etiket8.place(x = 450, y = 450)
        
        self.entry1 = tk.Entry(self)
        self.entry2 = tk.Entry(self)
        self.entry3 = tk.Entry(self)
        self.entry4 = tk.Entry(self)
        self.entry5 = tk.Entry(self, width = 5)
        self.entry1['state'] = 'disabled'
        self.entry2['state'] = 'disabled'
        self.entry3['state'] = 'disabled'
        self.entry4['state'] = 'disabled'
        
        self.entry1.place(x = 20, y = 120)
        self.entry2.place(x = 20, y = 220)
        self.entry3.place(x = 20, y = 320)
        self.entry4.place(x = 20, y = 420)
        self.entry5.place(x = 400, y = 403)
       
        self.buton = tk.Button(self, text = 'yeni bilgileri kaydet', command = lambda: self.kaydet())
        self.buton.place(x = 500, y = 400)
        
        self.buton2 = tk.Button(self, text = 'sec', command = lambda: self.sec())
        self.buton2.place(x = 450, y = 400)
        
        self.text = tk.Text(self, height = 10, width = 30)
        self.text.place(x = 450, y = 100)
        
        self.text2 = tk.Text(self, height = 10, width = 30)
        self.text2.place(x = 200, y = 100)

    def sec(self):
        self.etiket8['text'] = ''
        if self.entry5.get().isnumeric() == False:
            self.etiket8['text'] = "musteri no yanlis girildi"
            return
        no = int(self.entry5.get())
        if boyle_biri_var_mi(no, M) == 'yok': return
        self.entry1['state'] = 'normal'
        self.entry2['state'] = 'normal'
        self.entry3['state'] = 'normal'
        self.entry4['state'] = 'normal'
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        
        self.entry1.insert(0, M[no].isim)
        self.entry2.insert(0, M[no].soyad)
        self.entry3.insert(0, M[no].tcno)
        self.entry4.insert(0, sozlukteki_yerini_bul(A, M[no].araba))
        return        
    
    def kaydet(self):
        no = int(self.entry5.get())
        if self.entry1.get().isalpha() == False:
            self.etiket8['text'] =  "isim format yanlis?"
            return
        if self.entry2.get().isalpha() == False:
            self.etiket8['text'] =  "soyisim format yanlis"
            return
        if self.entry3.get().isnumeric() == False or len(self.entry3.get()) != 11:
            self.etiket6['text'] =  "TCno format yanlis"
            return
        M[no].tcno = self.entry3.get()
        if self.entry4.get().isnumeric() == False:
            self.etiket8['text'] = 'yanlis deger girildi'
            return
        if boyle_biri_var_mi(int(self.entry4.get()), A) == 'yok':
            self.etiket8['text'] = 'araba no yu kontrol et'
            return
        for val in A.values():
            if isinstance(val, Araba):
                if A[int(self.entry4.get())].durum != 'bos':
                    self.etiket8['text'] =  "bu araba zaten kullanilmakta"
                    return
        M[no].araba.durum = 'bos'
        M[no] = Musteri(self.entry1.get(), self.entry2.get(), self.entry3.get(), A[int(self.entry4.get())])
        A[int(self.entry4.get())].durum = 'dolu'
        goster(yenipencere.frames[MusteriDuzenle], M, Musteri)
        goster(yenipencere.frames[MusteriDuzenle], A, Araba, yenipencere.frames[MusteriDuzenle].text2)        
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.entry1['state'] = 'disabled'
        self.entry2['state'] = 'disabled'
        self.entry3['state'] = 'disabled'
        self.entry4['state'] = 'disabled'
        self.etiket8['text'] = 'bilgiler guncellendi'
        return
   
   
class ArabaDuzenle(MusteriDuzenle):
    def __init__(self, *args):
        MusteriDuzenle.__init__(self, *args)
        
        self.etiket['text'] = 'araba bilgisi degisme'
        self.etiket1['text'] = 'arabanin yeni plakasi'
        self.etiket2['text'] = 'arabanin yeni fiyati'
        self.text['height'] = 15
        self.text['width'] = 60
        self.text.place(x = 200, y = 100)
        self.entry1['state'] = 'disabled'
        self.entry2['state'] = 'disabled'
        self.entry3['state'] = 'normal'
        self.entry3['width'] = 5
        self.entry3.place(x = 400, y = 405)
        self.etiket3['text'] = "araba no'sunu bura gir -->"
        self.etiket3.place(x = 210, y = 405)
        for i in (self.etiket4, self.etiket5, self.entry4, self.text2, self.entry5, self.etiket7, self.etiket8):
            i.destroy()
        
        
    def sec(self):
        self.etiket6['text'] = ''
        if self.entry3.get().isnumeric() == False:
            self.etiket6['text'] = "araba no yanlis deger girildi"
            return
        no = int(self.entry3.get())
        if boyle_biri_var_mi(no, A) == 'yok': return
        self.entry1['state'] = 'normal'
        self.entry2['state'] = 'normal'
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry2.insert(0, A[no].fiyat)
        self.entry1.insert(0, A[no].plaka)
     
    def kaydet(self):
        if self.entry1.get() == '' or self.entry2.get == '':
            self.etiket6['text'] = 'lutfen bilgileri tam giriniz'
            return
        if self.entry2.get().isnumeric() == False:
            self.etiket6['text'] = "arabanin fiyati sadece sayi olmali"
            return
        no = int(self.entry3.get())
        A[no].fiyat = self.entry2.get()
        A[no].plaka = self.entry1.get()
        goster(yenipencere.frames[ArabaDuzenle], A, Araba)
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry1['state'] = 'disabled'
        self.entry2['state'] = 'disabled'
        self.etiket6['text'] = 'bilgiler guncellendi'


def entryler_dolu_mu(frame):
    for i in (frame.entry1.get(), frame.entry2.get(), frame.entry3.get(), frame.entry4.get()):
        if i == '':
            return "doludegil"
    return 'dolu'
    
    
def goster(frame, sozluk, sinif, txt = None):
    if txt == None:
        txt = frame.text
    txt.delete('1.0', 'end')
    for key, val in sozluk.items():
        if isinstance(val, sinif):
            a = str(key)+ '.' + str(val)
            txt.insert(tk.INSERT, "{}\n".format(a))

def boyle_biri_var_mi(no, sozluk):
    if sozluk == A:
        sinif = Araba
    else:
        sinif = Musteri
        
    if no in sozluk.keys():
        if isinstance(sozluk[no], sinif):
            return 'var'
        else:
            return 'yok'
    return 'yok'
        
def sozlukteki_yerini_bul(sozluk, nesne):
    for key, val in sozluk.items():
        if val is nesne:
            return key
    return "yok"

#
if __name__ == "__main__":
    giris_ekrani = AnaEkran()
    giris_ekrani.mainloop()

    yenipencere = YeniPencere()
    yenipencere.mainloop()
#

