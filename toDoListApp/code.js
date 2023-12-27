var girilen,secilen;
var eklenen,btnTamamla,btnsil,sonuc;

function listeyeEkle() { 
    girilen = document.getElementById("txtYapilacaklar").value;
    if (girilen!="") {
        eklenen = document.createElement("li");
        document.getElementById("listeYapilacaklar").appendChild(eklenen);
        eklenen.innerHTML=girilen;
        document.getElementById("sonuc").innerHTML="Listeye eklendi!";
        btnTamamla = document.createElement("img");
        eklenen.appendChild(btnTamamla);
        btnTamamla.setAttribute("src","image/tamam.png");
        btnTamamla.setAttribute("id","resimTamamla");
        //btnTamamla.setAttribute("onclick","tamamla();");
        btnTamamla.addEventListener("click",tamamla);
        btnSil = document.createElement("img");
        eklenen.appendChild(btnSil)
        btnSil.setAttribute("src","./image/sil.png");
        btnSil.setAttribute("id","resimSil");
        //btnTamamla.setAttribute("onclick","tamamla();");
        btnSil.addEventListener("click",sil);
    }
    else alert("Boş bırakılamaz");
}
function tamamla() { 
    eklenen = document.createElement("li");
    document.getElementById("listeTamamlananlar").appendChild(eklenen);
    secilen = event.currentTarget.parentNode;
    secilen.childNodes[1].style.display = "none";
    secilen.childNodes[2].setAttribute("onclick","sil();");
    eklenen.innerHTML = secilen.innerHTML;
    
    sil();

    document.getElementById("sonuc").innerHTML="Seçiminiz taşındı!";
}
function sil() { 
    secilen = event.currentTarget.parentNode;
    secilen.remove();
    document.getElementById("sonuc").innerHTML="Seçiminiz silindi!";
}