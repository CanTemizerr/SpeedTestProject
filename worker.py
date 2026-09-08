import time
from speed_test import SpeedTester
from storage import database
import sys

speed = SpeedTester()
db = database()

class otomation():
    def oto_test(self):
        try:
            zaman = int(input('PROGRAM KAÇ DAKİKA ÇALIŞSIN:    '))
            aralik = int(input('KAÇ DAKİKA ARALIK İLE HIZ TESTİ YAPSIN: '))
        except ValueError:
            print('Hata tam sayı giriniz!')
            sys.exit(1)


        if zaman <= 0 or aralik <= 0:
            print('Hata: süreler 0 dan büyük olmalıdır.')
        elif aralik >= zaman:
            print('Hata: Test aralığı çalışma süresinden küçük olmalıdır.')
        else:
            baslangic = time.time()

            while True:
                #program durdurma
                if time.time() - baslangic >= zaman*60:
                    print('program sonlandı.')
                    break


                #Hız testini yapıyoır
                try:
                    results = speed.run_test()
                except Exception as e:
                    print('Hata! ', e)

                #Veritabaına kaydetme
                try:
                    db.save_database(results)
                except Exception as e:
                    print('Hata! ', e)


                #aralık otomatık test yapma
                time.sleep(aralik * 60)











  



    
    