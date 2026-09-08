#Basic Pyhton Speed Test Analyzer
Speed test analyzer, internet hızını ölçen , sonuçları sqllite kaydeden ve istatistiksel analizler yaparak sonuçları grafikleştiren bir uygulamadır.

## Özellikler
-İnternet hız testi yapma
-Sonuçları sqllite kaydetme 
-Geçmiş sonuçlara bakma ve silme
-Pandas ile veri analizi ve grafikler ile görselleştirme
-Otomatik hiz testi yapma

## Kullanılan Teknolojiler
-Pandas
-speedtest-cli
-CSV OS modülleri
-Seaborn
-sqllite


## Kurulum
1.Projeyi bilgisayarınıza klonlayın veya indirin:


2.Proje klasorune gidin
cd SpeedTestProject
3.Sanal ortamı aktifleştirin
windows için:
venv\Scripts\activate
4.Gerekli kütüphaneleri yükleyin.(requirements.txt dosyasından):
pip install -r requirements.txt
5.Programı çalıştırın:
python main.py

## Proje Yapısı
SpeedTestProject/
│
├── main.py # Kullanıcı arayüzü ve ana döngü
├── speed_test.py # Hız testi işlemlerini yönetir
├── storage.py # CSV kayıt ve dosya temizleme işlemleri
├── analysis.py # Pandas ile veri analizi ve istatistikler
├── speed_result.csv # Test sonuçlarının saklandığı dosya
├── requirements.txt # Gerekli kütüphaneler listesi
└── README.md # Proje dokümantasyonu
## Örnek Çıkktı
1: hız testi yap
2: sonucu kaydet
3: analizler
4: tum sonucları goruntule
5: sonucları sil
6: cıkıs yap
## Eklencek özellikler
- JSON desteği
- SQLite/PostgreSQL veritabanı desteği
- PDF raporu oluşturma
- İnteraktif grafikler(plotly)
- Grafik oluşturma
- Otomatik zamanlanmış hız testleri
- Web arayüzü (Flask/FastAPI)
- Yapay zeka destekli hız analizi
- İnternet performansı hakkında öneriler sunan AI raporu
- Günlük, haftalık ve aylık otomatik raporlar
- Farklı internet sağlayıcılarının performans karşılaştırması
- Harita üzerinde konuma göre hız analizi
- E-posta ile otomatik rapor gönderme
- Kullanıcı hesap sistemi
- REST API desteği
- Docker ile tek komutla kurulum
- Bulut veritabanı desteği
- Karanlık (Dark Mode) tema
- Gerçek zamanlı performans izleme
- Ağ kesintilerini tespit edip bildirim gönderme
## Lisans
MIT License
