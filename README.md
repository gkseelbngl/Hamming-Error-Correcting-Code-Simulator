# Hamming Hata Düzeltme Kodu Simülatörü

<p align="center">
  <img src="images/hamming.png" alt="Hamming Error-Correcting Code" width="60%" height="60%">
</p>

## Genel Bakış

Bu Hamming Hata Düzeltme Kodu Simülatörü, kullanıcıların veri bitleri için Hamming kodları oluşturmasına, yapay hatalar eklemesine ve Hamming kodu ilkelerini kullanarak hataları tespit etmesine ve düzeltmesine olanak tanıyan bir Python uygulamasıdır. Uygulama, Tkinter ile oluşturulmuş bir grafik kullanıcı arayüzüne (GUI) sahiptir ve görüntüleri görüntülemek için Python Imaging Library (PIL) kullanır.

## Özellikler

- **Veri Boyutunu Seçin:** Veri girişiniz için veri boyutunu (4, 8 veya 16 bit) seçin.
- **Veri Bitlerini Girin:** Yalnızca 0 ve 1 içeren veri bitlerini girin.
- **Hamming Kodu Oluştur:** Girilen veri bitleri için Hamming kodunu otomatik olarak hesaplayın.
- **Hata Oluştur:** Belirli bir bit konumunda yapay bir hata oluşturun.
- **Hatayı Tespit Et ve Düzelt:** Hamming kodundaki hataları belirleyin ve düzeltin.

## Kurulum

1. **Depoyu Klonlayın**

   ```sh
   git clone https://github.com/yourusername/hamming-error-correcting-code-simulator.git
   cd hamming-error-correcting-code-simulator

2. **Bağımlılıkları Yükleyin**

   ```sh
   pip install tkinter pillow

3. **Uygulamayı Çalıştırın**

   ```sh
   python hamming_simulator.py

# Kullanım

1. **Veri Boyutunu Seçin:** Uygun veri boyutunu (4, 8 veya 16 bit) seçmek için radyo düğmelerini kullanın.
2. **Veri Bitlerini Girin:** Veri bitlerini sağlanan giriş alanına yazın.
3. **Hamming Kodunu Oluştur:** Girilen veri bitleri için Hamming kodunu oluşturmak için “Hamming Kodunu Oluştur” butonuna tıklayın.
4. **Hata Oluştur (İsteğe Bağlı):** Bir hatayı simüle etmek için bit konumunu girin ve hata türünü seçin (1'e çevir veya 0'a çevir). Hatayı tanıtmak için “Hata Tanıt” butonuna tıklayın.
5. **Hatayı Tespit Et ve Düzelt:** Hamming kodundaki hataları tespit etmek ve düzeltmek için “Hatayı Tespit Et ve Düzelt” butonuna tıklayın.

# Notlar

- Uygulama, veri bitlerindeki 1 bitlik hataları tespit edebilir ve düzeltebilir.
- “Hata Tespit Et ve Düzelt” işlevini kullanmadan önce hataları tanıttığınızdan emin olun.
- Hata tespit ve düzeltme süreci, hata konumunun ve türünün doğru bir şekilde belirlenmesine bağlıdır.

# Nasıl Çalışır?

Bu simülatör, veri bitlerine dayalı olarak Hamming kodlarını hesaplar ve test için yapay hatalar sunar. Hamming kodlarının hata düzeltme yeteneklerini göstermek için Hamming kodu üretimi ve hata düzeltme mantığı uygulanmaktadır.

# Teşekkür

- GUI bileşenleri için Tkinter kütüphanesi.
- Görüntü işleme için PIL (Pillow) kütüphanesi.
