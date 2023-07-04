// input variables

var urunTipi,urunFiyati,urunAdedi,urunTaksidi;

//Output variables

var araToplam,OdenecekToplamTutar,kargoUcreti=7;

//Global loop variables

var i;

// Global object variables

var liste,secenek;

//variables that store perfume information
var erkekParfumleri=["Celvin Clein",100,"Lacoste",120,"Axe",30,"First Class",50];
var kadinParfumleri=["Burbery",150,"Avon",80,"She",60,"Nina Ricci",130];

function urunAdediDoldur()
{
    for(i=1;i<=10;i++)
    {
        secenek=document.createElement("option");
        liste=document.getElementById("urunAdedi");
        liste.options.add(secenek);
        secenek.text=i;
        secenek.value=i;
    }
}

function urunTaksidiDoldur()
{
    for(i=0;i<=12;i=i+3)
    {
        secenek=document.createElement("option");
        liste=document.getElementById("urunTaksidi");
        liste.options.add(secenek);
        secenek.text=i;
        secenek.value=i;
    }
}


function urunleriGetir() {
    document.querySelectorAll("#urunListesi option").forEach(option=>option.remove()) 
    liste=document.getElementsByName("urunTipi")
    for(i=0;i<liste.length;i++){
        if (liste[i].checked) {
            urunTipi=liste[i].value;
        }
    }
    console.log(urunTipi)
    if(urunTipi=="E")
    {
        for(i=0;i<erkekParfumleri.length;i=i+2)
        {
            secenek=document.createElement("option");
            liste=document.getElementById("urunListesi");
            liste.options.add(secenek);
            secenek.text=erkekParfumleri[i];
            secenek.value=erkekParfumleri[i+1];
        }
    }

    else if(urunTipi=="K")
    {
        for(i=0;i<kadinParfumleri.length;i=i+2)
        {
            secenek=document.createElement("option");
            liste=document.getElementById("urunListesi");
            liste.options.add(secenek);
            secenek.text=kadinParfumleri[i];
            secenek.value=kadinParfumleri[i+1];
        }
    }
 }

 function hesapla() {
    liste = document.getElementById("urunListesi")
    urunSecimi =liste[liste.selectedIndex].value
    console.log(urunSecimi);

    liste=document.getElementById("urunAdedi");
    urunAdedi=liste[liste.selectedIndex].value;
    console.log(urunAdedi);

    liste=document.getElementById("urunTaksidi");
    urunTaksidi=liste[liste.selectedIndex].value;
    console.log(urunTaksidi);
    araToplam=urunSecimi*urunAdedi;

    if(urunTaksidi==3)
    {
        araToplam=araToplam*1.1;
    }
    else if(urunTaksidi==6)
    {
        araToplam=araToplam*1.2;
    }
    else if(urunTaksidi==9)
    {
        araToplam=araToplam*1.3;
    }
    else if(urunTaksidi==12)
    {
        araToplam=araToplam*1.4;
    }

    console.log(araToplam.toFixed(2));
    if (araToplam<100) {
        document.getElementById("txtKargo").value=kargoUcreti
        OdenecekToplamTutar+=kargoUcreti
    }

    else if(araToplam>=100){
        document.getElementById("txtKargo").value=0
          OdenecekToplamTutar=araToplam
    }
    
    console.log(OdenecekToplamTutar)
    document.getElementById("txtAraToplam").value=araToplam.toFixed(2);
    document.getElementById("txtBirimFiyat").value=urunSecimi;
    document.getElementById("sonuc").innerHTML="Ödemeniz gereken toplam tutarı(Vade farkı ve kargo dahil): "+OdenecekToplamTutar;
    
    
}