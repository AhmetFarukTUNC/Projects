//Tüm fonksiyonlarda kullanılmak üzere global nesne ve döngü değişkenleri
var liste=document.getElementById("listePizza"),secenek;
var i;

document.addEventListener("change",pizzaHesapla)

//Listelerden seçim yapılması olayını yakalayarak ilgili fonksiyonu çağırır
// document.addEventListener("change",pizzaHesapla);


function toggle()
{
    //İndirim kodu seçeneği seçili/değil ise text kutusunu aktif/pasif yapma
    liste=document.getElementsByName("grupIndirim");
    for(i=0;i<liste.length;i++)
    {
        if(liste[i].checked)
        {
            if(liste[i].value=="Aktif")
            {
                document.getElementById("txtIndirimKodu").disabled=false;
            }
            else if(liste[i].value=="Pasif")
            {
                document.getElementById("txtIndirimKodu").value=""
                document.getElementById("txtIndirimKodu").disabled=true;
                document.getElementById("dogrulama").innerHTML=""
                
            }
        }
    }

}

function pizzaHesapla()
{
    //Giriş ve çıkış verileri için değişkenler
    var pizzaFiyati,girilenKod,odenecekTutar;
    //Sabit indirim kodu tanımı
    const indirimKodu="PROMO";

    //Pizza fiyatını boyut listesinin value sinden alma
    liste=document.getElementById("listePizza");
    secenek=liste[liste.selectedIndex].value;
    pizzaFiyati=Number(secenek);

    //Ek malzeme seçimlerini alıp,fiyata +2 lira yansıtma
    liste=document.getElementsByName("grupEkMalzeme");
    // document.querySelectorAll('#listeEkSecimler option').forEach(option => option.remove());

    for(i=0;i<liste.length;i++)
    {

        if(liste[i].checked)
        {
            pizzaFiyati=pizzaFiyati+2;
            

            
        }


    }

    girilenKod=document.getElementById("txtIndirimKodu").value;

    //İndirim kodunu doğrulayıp indirim tutarını fiyata yansıtma
        
    if(indirimKodu==girilenKod)
        { 
            
            odenecekTutar=pizzaFiyati-5;
            
        }
    else
        {
            
            odenecekTutar=pizzaFiyati
            
            
        }
        //Sonucu yazdırma
        document.getElementById("sonuc").innerHTML="Ödenecek tutar: "+odenecekTutar;
    }

    
