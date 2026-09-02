import os 
from speed_test import SpeedTester
from storage import database
from visualization import analysis

speed=SpeedTester()
save  = database()
analysis = analysis()



while True:
    try:
       print("1:Hiz Testi Yap 2:Sonucu Kaydet 3:Sonuclari Sil 4:Cikis yap 5:İndirme hizi grafik")
       secilen_islem1=input("Seçim yapinziz")
       secilen_islem=int(secilen_islem1)
       if secilen_islem <= 0 or secilen_islem > 5:
           print("hatali deger")
           continue
    except Exception as e:
        print(f"hata {e}")
    if secilen_islem == 1:
        sonuclar=speed.run_test()
        print(sonuclar)
    elif secilen_islem == 2:
        try:
            save.save_database(sonuclar)
            print('Succesfull')
        except Exception as e:
            print('error' , e)
        else:
            print('Errorr')


    elif secilen_islem == 3:
        try:
            save.delete_db()
            print('Results was deleted')
        except Exception as e:
            print('error')
        
    elif secilen_islem == 4:
        break
    elif secilen_islem == 5:
        analysis.show_download_graph()

    





