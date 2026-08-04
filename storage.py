import csv
import os
class Csv_save():
    def __init__(self, dosya_adi="speed_result.csv"):
        self.dosya_adi=dosya_adi   
    def save_file(self,sonuc):
        #sonucları csv dosyasına kaydediyoruz.
        with open(self.dosya_adi, "a", newline="", encoding="utf-8") as dosya:
            yazici=csv.writer(dosya)
            yazici.writerow(sonuc.values())
        print("Sonuclar kaydedildi.")
    def delete_allfile(self):
        #dosyanın ıcındekı sonucları sılmek ıcın.
        if not os.path.exists(self.dosya_adi) or os.path.getsize(self.dosya_adi) == 0:
            print("Silinecek kayıt bulunamadı.")
        else:
            with open(self.dosya_adi, "w", newline="", encoding="utf-8"):
                pass
            print("Sonuclar silindi.")
               


