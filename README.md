# Hamming Hata Düzeltme Kodu Simülatörü

## Genel Bakış

Bu Hamming Hata Düzeltme Kodu Simülatörü, kullanıcıların veri bitleri için Hamming kodları oluşturmasına, yapay hatalar eklemesine ve Hamming kodu ilkelerini kullanarak hataları tespit etmesine ve düzeltmesine olanak tanıyan bir Python uygulamasıdır. Uygulama, Tkinter ile oluşturulmuş bir grafik kullanıcı arayüzüne (GUI) sahiptir ve görüntüleri görüntülemek için Python Imaging Library (PIL) kullanır.

## Özellikler

- **Veri Boyutunu Seçin**: Veri girişiniz için veri boyutunu (4, 8 veya 16 bit) seçin.
- Veri Bitlerini Girin**: Yalnızca 0 ve 1 içeren veri bitlerini girin.
- Hamming Kodu Oluştur**: Girilen veri bitleri için Hamming kodunu otomatik olarak hesaplayın.
- Hata Oluştur**: Belirli bir bit konumunda yapay bir hata oluşturun.
- Hatayı Tespit Et ve Düzelt**: Hamming kodundaki hataları belirleyin ve düzeltin.

## Kurulum

1. **Depoyu Klonlayın**

   ```sh
   git clone https://github.com/yourusername/hamming-error-correcting-code-simulator.git
   cd hamming-error-correcting-code-simulator

2. **Install Dependencies**

   ```sh
   pip install tkinter pillow

3. **Run the Application**

   ```sh
   python hamming_simulator.py

# Usage

1. *Select Data Size:* Use the radio buttons to select the appropriate data size (4, 8, or 16 bits).
