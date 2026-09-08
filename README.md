# 🚀 SpeedTestProject

Python ile geliştirilmiş, internet bağlantısının hızını ölçen, test sonuçlarını **SQLite veritabanında saklayan**, geçmiş sonuçları analiz eden ve grafiklerle görselleştiren bir internet hız testi uygulaması.

Proje; Python'da **modüler programlama, sınıflar, SQLite, veri analizi ve veri görselleştirme** konularını uygulamalı olarak kullanmak amacıyla geliştirilmiştir.

---

## ✨ Özellikler

* 🌐 İnternet hız testi yapma
* 📥 Download hızını ölçme
* 📤 Upload hızını ölçme
* 📡 Ping değerini ölçme
* 💾 Test sonuçlarını SQLite veritabanına kaydetme
* 🗑️ Kayıtlı sonuçları silme
* 📊 Geçmiş test sonuçlarını grafiklerle analiz etme
* 🤖 Otomatik / zamanlanmış hız testi çalıştırma
* 🕒 Test sonuçlarını tarih ve saat bilgisiyle saklama
* 🧩 Fonksiyon ve sınıflara ayrılmış modüler proje yapısı

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji         | Kullanım Alanı                             |
| ----------------- | ------------------------------------------ |
| **Python**        | Uygulamanın temel programlama dili         |
| **speedtest-cli** | İnternet hız testi                         |
| **SQLite**        | Test sonuçlarının kalıcı olarak saklanması |
| **Pandas**        | Veri analizi                               |
| **Seaborn**       | Veri görselleştirme                        |
| **Matplotlib**    | Grafiklerin oluşturulması                  |
| **datetime**      | Tarih ve saat işlemleri                    |

---

## 🏗️ Proje Yapısı

```text
SpeedTestProject/
│
├── main.py
├── speed_test.py
├── storage.py
├── visualization.py
├── worker.py
├── config.py
├── requirements.txt
├── speedtest.db
├── LICENSE
└── README.md
```

### 📄 Dosyaların Görevleri

**`main.py`**

Uygulamanın ana giriş noktasıdır.

Kullanıcı menüsünü yönetir ve diğer modüller arasındaki işlemleri koordine eder.

**`speed_test.py`**

İnternet hız testini gerçekleştirir.

Download, upload ve ping değerlerini ölçerek sonuçları Python sözlüğü şeklinde döndürür.

**`storage.py`**

SQLite veritabanı işlemlerini yönetir.

Test sonuçlarının:

* Kaydedilmesi
* Veritabanından yönetilmesi
* Silinmesi

gibi işlemler burada gerçekleştirilir.

**`visualization.py`**

Veritabanındaki sonuçları Pandas ile okuyarak analiz ve grafik işlemlerini gerçekleştirir.

**`worker.py`**

Otomatik hız testi işlemlerini yönetir.

**`config.py`**

Projede kullanılan yapılandırma bilgilerinin yönetilmesi için kullanılır.

**`speedtest.db`**

SQLite veritabanıdır ve yapılan hız testlerinin sonuçlarını saklar.

---

## ▶️ Kurulum

### 1. Projeyi klonla

```bash
git clone https://github.com/CanTemizerr/SpeedTestProject.git
```

### 2. Proje klasörüne gir

```bash
cd SpeedTestProject
```

### 3. Sanal ortam oluştur

```bash
python -m venv venv
```

### 4. Sanal ortamı aktifleştir

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 5. Gerekli kütüphaneleri yükle

```bash
pip install -r requirements.txt
```

### 6. Uygulamayı çalıştır

```bash
python main.py
```

---

## 🖥️ Kullanım

Program çalıştırıldığında kullanıcıya bir terminal menüsü sunulur:

```text
================================
          SPEED TEST
================================

1: Hız Testi Yap
2: Sonucu Kaydet
3: Sonuçları Sil
4: Grafikler
5: Otomatik Hız Testi
6: Çıkış
================================
```

### 1️⃣ Hız Testi

İnternet bağlantısının:

* Download
* Upload
* Ping

değerlerini ölçer.

Ölçüm tamamlandıktan sonra sonuç geçici olarak program içerisinde tutulur.

### 2️⃣ Sonucu Kaydet

Yapılan hız testinin sonuçlarını SQLite veritabanına kaydeder.

### 3️⃣ Sonuçları Sil

Veritabanında bulunan test sonuçlarının silinmesini sağlar.

### 4️⃣ Grafikler

Geçmiş test sonuçlarını Pandas kullanarak analiz eder ve Seaborn/Matplotlib ile görselleştirir.

Bu sayede internet bağlantısının zaman içerisindeki performansı incelenebilir.

### 5️⃣ Otomatik Hız Testi

Belirlenen çalışma mantığına göre otomatik hız testleri gerçekleştirilmesini sağlar.

Bu özellik sayesinde internet bağlantısının manuel olarak test edilmesine gerek kalmadan düzenli ölçümler yapılabilir.

---

## 🗄️ Veritabanı

Proje SQLite kullanmaktadır.

Temel olarak test sonuçları aşağıdaki bilgileri içerir:

```text
download
upload
ping
time
```

Örnek:

```text
Download: 92.45 Mbps
Upload:   18.32 Mbps
Ping:     24.17 ms
Time:     2026-09-08 21:30:15
```

Her yeni test sonucunun veritabanına eklenmesi sayesinde geçmiş performansın analiz edilmesi mümkün olur.

---

## 📊 Veri Analizi

Kayıtlı hız testi sonuçları Pandas kullanılarak işlenebilir.

Örneğin:

* Ortalama download hızı
* Ortalama upload hızı
* Ortalama ping
* En yüksek download
* En düşük download
* Zaman içerisindeki hız değişimi

gibi bilgiler analiz edilebilir.

Grafikler sayesinde internet bağlantısındaki performans değişimleri daha kolay takip edilebilir.

---

## 🎯 Projenin Amacı

Bu proje yalnızca bir internet hız testi yapmak için değil, Python ile gerçek bir uygulama geliştirirken farklı teknolojilerin birlikte nasıl kullanılabileceğini öğrenmek amacıyla geliştirilmiştir.

Projede özellikle aşağıdaki konuların pratik edilmesi hedeflenmiştir:

* Python'da OOP
* Modüler programlama
* SQLite veritabanı kullanımı
* Veri kaydetme ve okuma
* Pandas ile veri analizi
* Veri görselleştirme
* Otomasyon
* Hata yönetimi
* Proje yapısı ve modüller arası iletişim

---


---

## 📚 Öğrenme Amaçlı

Bu proje, bir bilgisayar mühendisliği öğrencisinin Python ve veri işleme konularındaki öğrendiklerini gerçek bir proje üzerinde uygulaması amacıyla geliştirilmiştir.

Projenin geliştirme sürecinde yeni özellikler eklenerek daha kapsamlı bir **network monitoring / internet performance analysis** uygulamasına dönüştürülmesi hedeflenmektedir.

---

## 📜 License

This project is licensed under the **MIT License**.

