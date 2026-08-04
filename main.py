import os 
from speed_test import SpeedTester
from storage import Csv_save
from analysis import Analysis1
speed=SpeedTester()
save=Csv_save()
analiz=Analysis1("speed_result.csv")


while True:
    try:
       print("1:Hiz Testi Yap 2:Sonucu Kaydet 3:Analizler 4:Tüm sonuclari goruntule 5:Sonucları Sil 6:Cikis yap")
       secilen_islem1=input("Seçim yapinziz")
       secilen_islem=int(secilen_islem1)
       if secilen_islem <= 0 or secilen_islem > 6:
           print("hatalı deger")
           continue
    except Exception as e:
        print(f"hata {e}")
    if secilen_islem == 1:
        sonuclar=speed.run_test()
        print(sonuclar)
    elif secilen_islem == 2:
        if "sonuclar" in locals():
            save.save_file(sonuclar)
        else:
            print("Önce hız testi yapın.")
    elif secilen_islem == 3:
        analiz.analizyap()
    elif secilen_islem == 4:
        analiz.allresult()
    elif secilen_islem == 5:
        save.delete_allfile()
    elif secilen_islem == 6:
        break
    





