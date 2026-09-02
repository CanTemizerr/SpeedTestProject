import pandas as pd
import seaborn as sns
from storage import database
import matplotlib.pyplot as plt

class analysis:
    def __init__(self):
        self.db = database()

    def get_data(self):
        return self.db.get_result()

    def show_download_graph(self):
        df = self.get_data()
        df['time'] = pd.to_datetime(df['time'])
        df['day'] = df['time'].dt.day
        df['hour'] = df['time'].dt.strftime('%H:%M')
        print('1:günlük grafik 2:saatlik grafik')
        secim = int(input('Bir sayı sec:'))
        if secim == 1:
            try:
                plt.figure(figsize=(12,6))
                sns.lineplot(
                    data=df,
                    x='day',
                    y='download',
                    palette='magma'
                )
                
                plt.xlabel('day')
                plt.ylabel('download')
                plt.title('Günlere Göre İndirme Hizi')
                plt.show()
            except:
                print('hata olustu')
        if secim == 2:
            try:
                plt.figure(figsize=(12,6))
                sns.lineplot(
                    data=df,
                    x='hour',
                    y='download',
                    palette='magma'
                )
                plt.xlabel('hour')
                plt.ylabel('download')
                plt.title('Günlere')
                plt.title('Saate Göre İndirme Hizi')
                plt.show()
            except:
                print('hata olustu')
        else:
            print('hatali deger')



