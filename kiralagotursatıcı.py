# görsel bir gui için tkinter importla...
import tkinter
#Bu class araba ve motor classın ebeveynidir
class satıcı:
    # bu metot yapıcı(conctructor)için oluştururlmuştur...
    def __init__(self,marka,model,depo,fiyat,renk):
        self.__marka=marka
        self.__model=model
        self.__depo=depo
        self.__fiyat=fiyat
        self.__renk=renk      
# Bu class motor child clasıdır ve satıcı classından miras alır...
class motor(satıcı):
    kuruluş="Bu uygulamadaki veriler 2023 verileridir"
    # bu metot yapıcı(conctructor)için oluştururlmuştur...
    def __init__(self,marka,model,depo,fiyat,renk):
        super().__init__(marka,model,depo,fiyat,renk)    
    # motorclassımızın class metodudur cls parametresini alır ve class daki herhangi bir değeri döndürmek için kullanılır...
    @classmethod
    def motoruygulamasıhakkında(cls):
        motor_paneli=tkinter.Tk()
        motor_paneli.state("zoomed")
        motor_paneli.title("Motorlu Araçlar Paneli")
        motor_paneli.config(bg="gray")
        welcome_label=tkinter.Label(motor_paneli,text="Motorlu Araçlar Paneline Hoşgeldiniz!",font="Verdana 32", bg="red", fg="white")
        welcome_label.place(x=400,y=100)
        buton1=tkinter.Button(motor_paneli,text="Motor Ekle",fg="white",bg="black",font="verdana 32",command=motor.motorbilgileriniekle)
        buton1.place(x=450,y=300,height=80,width=700)
        buton1=tkinter.Button(motor_paneli,text="Motor Bilgilerini Güncelle",fg="white",bg="black",font="verdana 32",command=motor.motorbilgileriniguncelle)
        buton1.place(x=450,y=500,height=80,width=700)
        print(cls.kuruluş)
    #Bu method motor bilgilerini alır ve ayrıca bu metotta sınıfa ait bir değer olmadığı için bu metot static bir metotdur.
    @staticmethod
    def motorbilgileriniekle():
        motoreklepenceresi=tkinter.Tk()
        motoreklepenceresi.state("zoomed")
        motoreklepenceresi.title("Motor Bilgilerini Ekleme Ekranı")
        motoreklepenceresi.config(bg="gray")
        açılış_yazısı=tkinter.Label(motoreklepenceresi,text="Motor Ekleme Portalına Hoşgeldiniz!",font="Verdana 32", bg="red", fg="white")
        açılış_yazısı.place(x=400,y=100)
        yazi=tkinter.Label(motoreklepenceresi,text="Marka : ",font="Verdana 15", bg="red", fg="white")
        yazi.place(x=230,y=280)
        yazi_2=tkinter.Label(motoreklepenceresi,text="Model : ",font="Verdana 15", bg="red", fg="white")
        yazi_2.place(x=230,y=330)
        yazi_3=tkinter.Label(motoreklepenceresi,text="Depo : ",font="Verdana 15", bg="red", fg="white")
        yazi_3.place(x=230,y=380)
        yazi_4=tkinter.Label(motoreklepenceresi,text="Fiyat : ",font="Verdana 15", bg="red", fg="white")
        yazi_4.place(x=230,y=430)
        yazi_5=tkinter.Label(motoreklepenceresi,text="Renk : ",font="Verdana 15", bg="red", fg="white")
        yazi_5.place(x=230,y=480)
        marka=tkinter.Entry(motoreklepenceresi,bg="white", fg="black", font="verdana 17 bold")
        marka.place(x=330, y=280, width=900, height=30)
        model=tkinter.Entry(motoreklepenceresi,bg="white",fg="black",font="verdana 17 bold")
        model.place(x=330, y=330, width=900, height=30)
        depo=tkinter.Entry(motoreklepenceresi,bg="white",fg="black",font="verdana 17 bold")
        depo.place(x=330, y=380, width=900, height=30)
        fiyat=tkinter.Entry(motoreklepenceresi,bg="white",fg="black",font="verdana 17 bold")
        fiyat.place(x=330, y=430, width=900, height=30)
        renk=tkinter.Entry(motoreklepenceresi,bg="white",fg="black",font="verdana 17 bold")
        renk.place(x=330, y=480, width=900, height=30)
        def eklemeyazısı():
            açılış_yazısı=tkinter.Label(motoreklepenceresi,text="Tüm Bilgiler Veri Tabanına Eklenmiştir...",font="Verdana 32", bg="red", fg="white")
            açılış_yazısı.place(x=300,y=560)
        buton1=tkinter.Button(motoreklepenceresi,text="Oluştur",fg="white",bg="black",font="verdana 32",command=eklemeyazısı)
        buton1.place(x=650,y=640)
    #Bu metot motor bilgilerini günceller...
    def motorbilgileriniguncelle(self):
        motor_guncelleme_penceresi=tkinter.Tk()
        motor_guncelleme_penceresi.state("zoomed")
        motor_guncelleme_penceresi.title("Motor Bilgilerini Güncelleme Ekranı")
        motor_guncelleme_penceresi.config(bg="gray")
        yazi=tkinter.Label(motor_guncelleme_penceresi,text="Motor Bilgilerini Güncelleme Portalına Hoşgeldiniz!",font="Verdana 32", bg="red", fg="white")
        yazi.place(x=250,y=150)
        self.yazi=tkinter.Label(motor_guncelleme_penceresi,text="Güncellenecek Bölüm : ",font="Verdana 15", bg="red", fg="white")
        self.yazi.place(x=130,y=300)
        key=tkinter.Entry(motor_guncelleme_penceresi,bg="white", fg="black", font="verdana 17 bold")
        key.place(x=400, y=300, width=900, height=30)
        value=tkinter.Label(motor_guncelleme_penceresi,text="Yeni Değer : ",font="Verdana 15", bg="red", fg="white")
        value.place(x=130,y=450,width=250)
        value=tkinter.Entry(motor_guncelleme_penceresi,bg="white", fg="black", font="verdana 17 bold")
        value.place(x=400, y=450, width=900, height=30)
        def eklemeyazısı2():
            uyarı=tkinter.Label(motor_guncelleme_penceresi,text="Yeni bilgiler veri tabanına kaydedilmiştir...",font="Verdana 32", bg="red", fg="white")
            uyarı.place(x=350,y=530)
        
        butonduzenle=tkinter.Button(motor_guncelleme_penceresi,text="Düzenle",fg="white",bg="black",font="verdana 32",command=eklemeyazısı2)
        butonduzenle.place(x=650,y=630)

motor=motor("","",100,1000,"")
# bu sınıf araba sınıfıdır ve satıcı classından miras alır...
class araba(satıcı):
    def __init__(self, marka, model,depo,fiyat,renk):
        super().__init__(marka, model,depo,fiyat,renk)
    # bu metot araba ekleme ekranını oluşturmak amacıyla kodlanmıştır...
    def arababilgileriniekle(self):
        araba_ekle_penceresi=tkinter.Tk()
        araba_ekle_penceresi.state("zoomed")
        araba_ekle_penceresi.title("Araba ekleme ekranı")
        araba_ekle_penceresi.config(bg="gray")
        açılış_yazısı=tkinter.Label(araba_ekle_penceresi,text="Araba Ekleme Portalına Hoşgeldiniz!",font="Verdana 32", bg="red", fg="white")
        açılış_yazısı.place(x=400,y=100)
        self.yazi=tkinter.Label(araba_ekle_penceresi,text="Marka : ",font="Verdana 15", bg="red", fg="white")
        self.yazi.place(x=230,y=280)
        self.yazi_2=tkinter.Label(araba_ekle_penceresi,text="Model : ",font="Verdana 15", bg="red", fg="white")
        self.yazi_2.place(x=230,y=330)
        self.yazi_3=tkinter.Label(araba_ekle_penceresi,text="Depo : ",font="Verdana 15", bg="red", fg="white")
        self.yazi_3.place(x=230,y=380)
        self.yazi_4=tkinter.Label(araba_ekle_penceresi,text="Fiyat : ",font="Verdana 15", bg="red", fg="white")
        self.yazi_4.place(x=230,y=430)
        self.yazi_5=tkinter.Label(araba_ekle_penceresi,text="Renk : ",font="Verdana 15", bg="red", fg="white")
        self.yazi_5.place(x=230,y=480)
        self.marka=tkinter.Entry(araba_ekle_penceresi,bg="white", fg="black", font="verdana 17 bold")
        self.marka.place(x=330, y=280, width=900, height=30)
        self.model=tkinter.Entry(araba_ekle_penceresi,bg="white",fg="black",font="verdana 17 bold")
        self.model.place(x=330, y=330, width=900, height=30)
        self.depo=tkinter.Entry(araba_ekle_penceresi,bg="white",fg="black",font="verdana 17 bold")
        self.depo.place(x=330, y=380, width=900, height=30)
        self.fiyat=tkinter.Entry(araba_ekle_penceresi,bg="white",fg="black",font="verdana 17 bold")
        self.fiyat.place(x=330, y=430, width=900, height=30)
        self.renk=tkinter.Entry(araba_ekle_penceresi,bg="white",fg="black",font="verdana 17 bold")
        self.renk.place(x=330, y=480, width=900, height=30)
        def eklemeyazısı():
            açılış_yazısı=tkinter.Label(araba_ekle_penceresi,text="Tüm Bilgiler Veri Tabanına Eklenmiştir...",font="Verdana 32", bg="red", fg="white")
            açılış_yazısı.place(x=300,y=530)
        buton1=tkinter.Button(araba_ekle_penceresi,text="Oluştur",fg="white",bg="black",font="verdana 32",command=eklemeyazısı)
        buton1.place(x=650,y=600)
    # bu metot araba guncelleme ekranı oluşturmak amacıyla oluşturulmuştur...
    def arababilgileriniguncelle(self):
        araba_guncelleme_penceresi=tkinter.Tk()
        araba_guncelleme_penceresi.state("zoomed")
        araba_guncelleme_penceresi.title("Araba güncelleme ekranı")
        araba_guncelleme_penceresi.config(bg="gray")
        yazihosgeldin=tkinter.Label(araba_guncelleme_penceresi,text="Araba Guncelleme Portalına Hoşgeldiniz!",font="Verdana 32", bg="red", fg="white")
        yazihosgeldin.place(x=350,y=150)
        guncelenecekdeğer=tkinter.Label(araba_guncelleme_penceresi,text="Güncellenecek Bölüm : ",font="Verdana 15", bg="red", fg="white")
        guncelenecekdeğer.place(x=180,y=300)
        guncelenecekdeğer=tkinter.Entry(araba_guncelleme_penceresi,bg="white", fg="black", font="verdana 17 bold")
        guncelenecekdeğer.place(x=450, y=300, width=900, height=30)
        gunceldeger=tkinter.Label(araba_guncelleme_penceresi,text="Yeni Değer : ",font="Verdana 15", bg="red", fg="white")
        gunceldeger.place(x=180,y=450,width=240)
        gunceldegergiris=tkinter.Entry(araba_guncelleme_penceresi,bg="white", fg="black", font="verdana 17 bold")
        gunceldegergiris.place(x=450, y=450, width=900, height=30)
        def eklemeyazısı2():
            self.yazi=tkinter.Label(araba_guncelleme_penceresi,text="Yeni bilgiler veri tabanına kaydedilmiştir...",font="Verdana 32", bg="red", fg="white")
            self.yazi.place(x=350,y=515)
        
        buton1=tkinter.Button(araba_guncelleme_penceresi,text="Düzenle",fg="white",bg="black",font="verdana 32",command=eklemeyazısı2)
        buton1.place(x=650,y=600)
araba=araba("",0,0,0,"kırmızı")
# bu metot araba işlemleri sayfası için oluşturulmuştur...
def araba_işlemleri():
    iç_pencere_araba=tkinter.Tk()
    iç_pencere_araba.title("Araba İşlemleri")
    iç_pencere_araba.state("zoomed")
    iç_pencere_araba.config(bg="gray")
    yazi=tkinter.Label(iç_pencere_araba,text="Araba işlemleri Portalına hoşgeldiniz!",font="Verdana 32", bg="red", fg="white")
    yazi.place(x=400,y=100)
    buton1=tkinter.Button(iç_pencere_araba,text="Araba Ekle",fg="white",bg="black",font="verdana 32",command=araba.arababilgileriniekle)
    buton1.place(x=650,y=300)
    buton2=tkinter.Button(iç_pencere_araba,text="Araba Bilgilerini güncelle",fg="white",bg="black",font="verdana 32",command=araba.arababilgileriniguncelle)
    buton2.place(x=500,y=500)
    iç_pencere_araba.mainloop()
#bu metot satıcı portalı için oluşturulmuştur...
def uygulama():
    satıcı_penceresi=tkinter.Tk()
    satıcı_penceresi.title("Satıcı Portalı")
    satıcı_penceresi.state("zoomed")
    satıcı_penceresi.config(bg="gray")
    yazi=tkinter.Label(satıcı_penceresi,text="Satıcı Portalına hoşgeldiniz!",font="Verdana 32", bg="red", fg="white")
    yazi.place(x=475,y=200)
    buton1=tkinter.Button(satıcı_penceresi,text="Araba İşlemleri",fg="white",bg="black",font="verdana 32",command=araba_işlemleri)
    buton1.place(x=250,y=400)
    buton2=tkinter.Button(satıcı_penceresi,text="Motor İşlemleri",fg="white",bg="black",font="verdana 32",command=motor.motoruygulamasıhakkında)
    buton2.place(x=900,y=400)
    satıcı_penceresi.mainloop()
uygulama()

    


