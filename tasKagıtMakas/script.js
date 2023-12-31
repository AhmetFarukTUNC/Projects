function oyunuBaslat(secim){
    // önce seçim değişkene akatarılır...
    
    let kullaniciSecimi = secim.id;

    console.log(kullaniciSecimi);

    // Bilgisayar tarafından oluşturulan random sayıya indis olarak sahip olan dizi elemanı değişkene aktarılır bu değer bilgisayarın seçimidir...

    let rastgeleSayi = Math.floor(Math.random()*3);

    let bilgisayarSecimi = ["tas","kagit","makas"][rastgeleSayi];

    console.log(bilgisayarSecimi);

    //Puanlamaları dizi şeklinde değişkene aktaralım...

    let oyunPuanlamalari = {
        "tas" : {"makas":1,"tas":0.5,"kagit":0},
        "kagit" : {"tas":1,"kagit":0.5,"makas":0},
        "makas" : {"kagit":1,"makas":0.5,"tas":0}
    };

    //Dizi seçimimize karşılık gelen puanı alalım...
    let kullaniciPuani = oyunPuanlamalari[kullaniciSecimi][bilgisayarSecimi];

    console.log(kullaniciPuani);

    //Kayıtlı tüm resimlerin kaynak adresleri alınır...
    
    let kayitliResimler = {
        "tas" : document.getElementById("tas").src,
        "kagit":document.getElementById("kagit").src,
        "makas":document.getElementById("makas").src
 
    }

    // sonuc için sayfadaki tüm resimler kaldırılır...

    document.getElementById("tas").remove();

    document.getElementById("kagit").remove();

    document.getElementById("makas").remove();

    //bilgisayar seçimi,kullanıcı seçimi ve sonuc ekrana bastırmak için yeni nesneler oluşturulur...
    
    let kullaniciResmi = document.createElement("img");

    let bilgisayarResmi = document.createElement("img");

    let sonucMesajı = document.createElement("div");

    // Resim nesnelerine seçimlere göre uygun src yolları bind edilir...

    kullaniciResmi.src = kayitliResimler[kullaniciSecimi]

    bilgisayarResmi.src = kayitliResimler[bilgisayarSecimi];

    // container içine oluşturulan nesnelerin monte edilmesi işlemei tanımlanır...

    document.getElementById("container").appendChild(kullaniciResmi);
    document.getElementById("container").appendChild(sonucMesajı);
    document.getElementById("container").appendChild(bilgisayarResmi);

    
    
    // Şart döngüleriyle sonuç ekrana yazdırılır...

    if (kullaniciPuani === 0) {
        sonucMesajı.innerHTML = "Üzgünüz!Kaybettiniz. :( ";
        sonucMesajı.style.color = "red";
        sonucMesajı.style.fontSize = "2rem";
    }

    else if (kullaniciPuani === 0.5) {
        sonucMesajı.innerHTML = "Sonuç berabere!";
        sonucMesajı.style.color = "blue";
        sonucMesajı.style.fontSize = "2rem";
    }

    else{
        sonucMesajı.innerHTML = "Tebrikler kazandınız! :)";
        sonucMesajı.style.color = "green";
        sonucMesajı.style.fontSize = "0.4rem";
    }



}