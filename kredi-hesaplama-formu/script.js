function kredihesapla(){
    var cekilecektutar,vadesayisi;
    var aylıktaksit,odenecektoplamtutar;
    cekilecektutar =document.getElementById("txtkreditutarı").value
    var liste = document.getElementById("listevade")
    vadesayisi=liste.options[liste.selectedIndex].value;
    if (vadesayisi==12) {
        odenecektoplamtutar=cekilecektutar*1.1
    }
    else if (vadesayisi==24) {
        odenecektoplamtutar=cekilecektutar*1.2
    }
    else if (vadesayisi==36) {
        odenecektoplamtutar=cekilecektutar*1.3
    }
    else if (vadesayisi==48) {
        odenecektoplamtutar=cekilecektutar*1.4
    }
    
    aylıktaksit=odenecektoplamtutar/vadesayisi
    document.querySelector("#sonuc").innerHTML="Geri Ödeme Toplamı : "+odenecektoplamtutar+" TL"+"<br>"+
    "Aylık Taksit Tutarınız : " +aylıktaksit.toFixed(2)+" TL"
    

  }