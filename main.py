import os 
from speed_test import SpeedTester
from storage import database
from visualization import analysis
from worker import otomation

speed=SpeedTester()
save  = database()
graph = analysis()
oto = otomation()

sonuclar = None

def menu():
    print('\n================================')
    print('         SPEED TEST')
    print('================================')
    print('1: Hız Testi yap')
    print('2: Sonucu Kaydet')
    print('3: Sonuçlari Sil')
    print('4: Grafikler')
    print('5: Otomatik hiz testi')
    print('6: Çıkış')
    print('================================')


while True:
    menu()

    try:
        secilen_islem = int(input('Seçim yapiniz: '))

        if secilen_islem < 1 or secilen_islem > 6:
            print('Hatali değer!')
            continue
    except ValueError:
        print('Lütfen sayı giriniz')
        continue

    if secilen_islem == 1:
        try:
            print('Hız testi yapılıyor.....')
            sonuclar = speed.run_test()
            print('Hiz testi başarili')
            print(sonuclar)
        except Exception as e:
            print('hata olustu: ', e)

    elif secilen_islem == 2:
        if sonuclar is None:
            print('Önce hiz testi yap!!!!')
        else:
            try:
                save.save_database(sonuclar)
                print('Sonuçlar basarıyla kaydedildi')
            except Exception as e:
                print('Hata: ', e)

    elif secilen_islem == 3:
        try:
            save.delete_db()
            print('sonuclar silindi')
        except Exception as e:
            print('hata: ', e)

    elif secilen_islem == 4:
        graph.show_graph()

    elif secilen_islem == 5:
        oto.oto_test()

    elif secilen_islem == 6:
        print('Çıkış yapılıyor....')
        break

    




    





