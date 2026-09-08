import pandas as pd
import seaborn as sns
from storage import database
import matplotlib.pyplot as plt

class analysis:
    def __init__(self):
        self.db = database()

    def get_data(self):
        return self.db.get_result()

    def show_graph(self):
        try:
            df = self.get_data()
            df['time'] = pd.to_datetime(df['time'])
            df['day'] = df['time'].dt.day
            df['hour'] = df['time'].dt.strftime('%H:%M')

            print("1: Download\n 2: Upload\n 3: Ping\n")
            try:
                secim = int(input("Grafik Türü: "))
            except ValueError:
                print('Hatali Değer')
                return

            if secim == 1:
                y = 'download'
                baslik = 'Download hizi'
            elif secim == 2:
                y = 'upload'
                baslik = 'Upload hizi'
            elif secim == 3:
                y = 'ping'
                baslik = 'Ping'

            print('1: Saatlik\n 2: Günlük')

            try:
                zaman = int(input('Zaman secimi: '))
            except ValueError:
                print('hatali değer')
                return

            if zaman == 1:
                x= 'hour'
                xlabel = 'saat'

            elif zaman ==2:
                x= 'time'
                xlabel = 'tarih'

            try:
                plt.figure(figsize=(12, 6))

                sns.lineplot(
                    data=df,
                    x=x,
                    y=y
                )
                plt.xlabel(xlabel)
                plt.ylabel(y)
                plt.title(baslik)
                plt.show()
            except Exception as e:
                print('Grafik oluşturulırken hata oluştu:', e)
        except Exception as e:
            print('Veriler alınırken hata olustu:', e)
            
                
            
    
                


        


    



