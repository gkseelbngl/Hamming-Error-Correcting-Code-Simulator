import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import math

# Veri boyutları
data_sizes = [4, 8, 16]

# Hata pozisyonlarının listesi
error_positions = []

# Tema renkleri
dark_bg = "#1E1E1E"
light_fg = "#FFFFFF"
button_bg = "#3700B3"

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Hamming Error-Correcting Code Simülatörü")
root.iconbitmap("ico/Hamming.ico")
root.configure(bg=dark_bg)
root.geometry("330x500+1000+120")

# Pencere boyutunu sabit tut
root.resizable(False, False)

# Hamming.png resmini yükle ve boyutlandır
img = Image.open("images/hamming.png")
img = img.resize((290, 80))
hamming_img = ImageTk.PhotoImage(img)

# Resim etiketi oluştur
img_label = tk.Label(root, image=hamming_img, bg="#1E1E1E")
img_label.grid(row=0, column=0, columnspan=2, pady=10)


# İmleci soru işareti şekline dönüştürecek fonksiyon
def change_cursor(event):
    img_label.config(cursor="question_arrow")


# İmleç olaylarını bağla
img_label.bind("<Enter>", change_cursor)
img_label.bind("<Leave>", lambda event: img_label.config(cursor=""))


# Bilgi mesajı gösteren fonksiyon
def show_info(event):
    messagebox.showinfo(
        "Nasıl Çalışır?",
        """Hamming Hatası Düzeltme Kodu Simülatörü'ne hoş geldiniz!

Bu simülatör, veri bitleri için Hamming kodlarını hesaplamanıza ve yapay hatalar oluşturarak hatayı tespit etme ve düzeltme yeteneğini test etmenize olanak tanır.

Kullanım Adımları:

1. Veri Boyutunu Seçin: Veri girişinin uzunluğuna uygun veri boyutunu seçin.
2. Veri Bitlerini Girin: Veri girişine yalnızca 0 ve 1 içeren veri bitlerini girin.
3. Hamming Kodu Oluştur: Veri bitleri için Hamming kodunu otomatik olarak hesaplamak için "Hamming Kodu Üret" butonuna tıklayın.
4. Hata Oluştur (Opsiyonel): Yapay hata oluşturmak için "Hata Bit Konumu" ve "Hata Türü"nü seçin ve "Hata Oluştur" butonuna tıklayın.
5. Hata Tespit et ve Düzelt: Hamming kodundaki hatayı tespit etmek ve düzeltmek için "Hata Tespit et ve Düzelt" butonuna tıklayın.

Notlar:

* Hata tespit ve düzeltme işlemi, hata konumunun ve türünün doğru şekilde belirlenmesine bağlıdır.
* Hamming Kodu, veri bitlerinde en fazla 1 bitlik hata tespit ve düzeltme sağlayabilir.
* Veri giriş alanı, sadece 0 ve 1 içermelidir. Girilen veri boyutu, seçilen veri boyutuyla eşleşmelidir.
* Hata bit konumu, Hamming kodu uzunluğu içinde olmalıdır.
""",
    )


# Resim etiketi için tıklama olayını bağla
img_label.bind("<Button-1>", show_info)


# Fonksiyonlar
def calculate_hamming_code(data):
    """
    Verilen veri bitleri için Hamming kodunu hesaplar.
    """
    data_bits = len(data)
    parity_bits = 0

    # Parite bitlerinin sayısını hesapla
    while (2**parity_bits) < (data_bits + parity_bits + 1):
        parity_bits += 1

    total_bits = data_bits + parity_bits
    hamming_code = [0] * total_bits

    j = 0
    k = 0
    for i in range(1, total_bits + 1):
        if i == 2**j:
            j += 1
        else:
            hamming_code[i - 1] = data[k]
            k += 1

    # Parite bitlerini hesapla
    for i in range(parity_bits):
        parity_pos = 2**i
        parity = 0
        for j in range(1, total_bits + 1):
            if j & parity_pos:
                parity ^= hamming_code[j - 1]
        hamming_code[parity_pos - 1] = parity

    return hamming_code


def check_and_correct_hamming_code(received_data):
    """
    Hata sendromunu tespit eder, hata konumunu ve türünü belirler ve hatayı düzeltir.
    """
    total_bits = len(received_data)
    parity_bits = int(math.log2(total_bits)) + 1
    error_position = 0

    # Hata konumunu hesapla
    for i in range(parity_bits):
        parity_pos = 2**i
        parity = 0
        for j in range(1, total_bits + 1):
            if j & parity_pos:
                parity ^= received_data[j - 1]
        if parity != 0:
            error_position += parity_pos

    if error_position == 0:
        return received_data, None
    else:
        # Hata konumunu 1 tabanlı indekse dönüştür
        error_position -= 1
        # Hata düzeltme işlemi
        if error_position < total_bits:
            received_data[error_position] ^= 1
        return received_data, error_position + 1  # 1 tabanlı indekse geri dönüş


def introduce_error():
    """
    Verilen bit konumunda yapay hata oluşturur.
    """
    ham_code = ham_code_entry.get().strip()
    bit_num = error_bit_entry.get().strip()

    if not bit_num.isdigit():
        messagebox.showerror("Hata", "Lütfen hata yapılacak bit konumunu girin.")
        return

    bit_num = int(bit_num)
    if bit_num < 1 or bit_num > len(ham_code.split()):
        messagebox.showerror("Hata", "Geçersiz bit konumu.")
        return

    bit_num -= 1  # Kullanıcıdan alınan indeksi 0 tabanlı indekse dönüştür

    if bit_num in error_positions:
        messagebox.showerror("Hata", "Bu bit konumunda zaten hata var.")
        return

    ham_code_list = list(map(int, ham_code.split()))
    error_type = error_type_var.get()

    # Hata tipine göre bit değerini değiştir
    if error_type == "1'e Çevir":
        ham_code_list[bit_num] = "1"
    elif error_type == "0'a Çevir":
        ham_code_list[bit_num] = "0"

    error_positions.append(bit_num)
    ham_code_entry.delete(0, tk.END)
    ham_code_entry.insert(0, " ".join(map(str, ham_code_list)))
    messagebox.showinfo(
        "Başarı", f"{bit_num + 1}. bitte {error_type} hatası oluşturuldu."
    )


def detect_and_correct_error():
    """
    Hata sendromunu tespit eder, hata konumunu ve türünü belirler ve hatayı düzeltir.
    """
    # Hata konumlarının boş olup olmadığını kontrol edin
    if not error_positions:
        messagebox.showerror("Hata", "Önce hata oluşturmalısınız.")
        return

    received_data = list(map(int, ham_code_entry.get().split()))
    corrected_data, error_position = check_and_correct_hamming_code(received_data)

    if error_position is None:
        messagebox.showinfo("Başarı", "Hamming kodunda hata yok.")
    elif error_position > len(received_data):
        messagebox.showinfo("Bilgi", "Hata tespit edilemez.")
    else:
        ham_code_entry.delete(0, tk.END)
        ham_code_entry.insert(0, " ".join(map(str, corrected_data)))
        messagebox.showinfo(
            "Başarı",
            f"{error_position}. bitte hata düzeltildi. Düzeltilmiş Hamming Kodu: {' '.join(map(str, corrected_data))}",
        )


def generate_hamming_code():
    """
    Veri bitlerinden manuel olarak Hamming kodu hesaplar.
    """
    data = (
        data_entry.get().strip()
    )  # Veri girişini al ve başındaki ve sonundaki boşlukları kaldır
    if not all(bit in ["0", "1"] for bit in data):
        messagebox.showerror(
            "Hata", "Lütfen yalnızca 0 ve 1 içeren veri bitlerini girin."
        )
        return

    data_size = len(data)

    if data_size not in data_sizes:
        messagebox.showerror("Hata", f"Geçersiz veri boyutu: {data_size} bit.")
        return

    # Veriyi listeye dönüştür
    data_list = list(map(int, data))

    ham_code = calculate_hamming_code(data_list)
    ham_code_entry.delete(0, tk.END)
    ham_code_entry.insert(0, " ".join(map(str, ham_code)))
    messagebox.showinfo("Başarı", "Hamming kodu başarıyla üretildi.")

    # Hamming kodunu başarıyla oluşturduktan sonra hata düğmelerini etkinleştirir
    introduce_error_button.config(state=tk.NORMAL)
    detect_and_correct_button.config(state=tk.NORMAL)


def validate_data_length(*args):
    """
    Veri girişinin uzunluğunu doğrular ve butonu etkinleştirir veya devre dışı bırakır.
    """
    data = data_entry.get().strip()  # Verinin başındaki ve sonundaki boşlukları kaldır
    data_size = len(data)
    selected_size = selected_data_size.get()

    # Yalnızca 0 ve 1 içeren veri girişini doğrula
    if all(bit in ["0", "1"] for bit in data) and data_size == selected_size:
        generate_code_button.config(state=tk.NORMAL)
    else:
        generate_code_button.config(state=tk.DISABLED)


# Pencerenin kapatılması işlemini işlemek için fonksiyon
def on_closing():
    """
    Pencerenin kapatılması işlemini işler.
    """
    if messagebox.askokcancel("Çıkış", "Uygulamadan çıkmak istiyor musunuz?"):
        root.destroy()


# Arayüz Elemanları

# Veri boyutunu seçme menüsü
selected_data_size = tk.IntVar(value=4)  # Varsayılan olarak ilk boyut seçili

data_size_label = tk.Label(root, text="Veri Boyutu:", bg=dark_bg, fg=light_fg)
data_size_label.grid(row=1, column=0, padx=10, pady=10)

data_size_frame = tk.Frame(root, bg=dark_bg)
data_size_frame.grid(row=1, column=1, padx=10, pady=10)

for size in data_sizes:
    radio_button = tk.Radiobutton(
        data_size_frame,
        text=f"{size} bit",
        variable=selected_data_size,
        value=size,
        bg=dark_bg,
        fg=light_fg,
        selectcolor=dark_bg,
        command=validate_data_length,
    )
    radio_button.pack(side=tk.LEFT, padx=5)

# Veri giriş alanı
data_label = tk.Label(root, text="Veri Bitleri:", bg=dark_bg, fg=light_fg)
data_label.grid(row=2, column=0, padx=10, pady=10)
data_entry = tk.Entry(
    root, validate="key", width=20, bg="#778899", font=("Helvetica", 10, "bold")
)
data_entry.grid(row=2, column=1, padx=10, pady=10)
data_entry.bind("<KeyRelease>", validate_data_length)

# Hamming kodu gösterme alanı
ham_code_label = tk.Label(root, text="Hamming Kodu:", bg=dark_bg, fg=light_fg)
ham_code_label.grid(row=3, column=0, padx=10, pady=10)
ham_code_entry = tk.Entry(root, width=20, bg="#778899", font=("Helvetica", 10, "bold"))
ham_code_entry.grid(row=3, column=1, padx=10, pady=10)

# Hata bit konumu giriş alanı
error_bit_label = tk.Label(root, text="Hata Bit Konumu:", bg=dark_bg, fg=light_fg)
error_bit_label.grid(row=4, column=0, padx=10, pady=10)
error_bit_entry = tk.Entry(root, width=20, bg="#778899", font=("Helvetica", 10, "bold"))
error_bit_entry.grid(row=4, column=1, padx=10, pady=10)

# Hata Türü Seçimi için Radiobutton'lar
error_type_label = tk.Label(root, text="Hata Türü:", bg=dark_bg, fg=light_fg)
error_type_label.grid(row=5, column=0, padx=10, pady=10)

# Başlangıçta seçili olmayacak
error_type_var = tk.StringVar(value="1'e Çevir")

# "1'e Çevir" Butonu
error_type_1_button = tk.Radiobutton(
    root,
    text="1'e Çevir",
    variable=error_type_var,
    value="1'e Çevir",
    bg=dark_bg,
    fg=light_fg,
    selectcolor=dark_bg,
    state=tk.DISABLED,  # Başlangıçta pasif
)
error_type_1_button.grid(row=5, column=1, padx=5, pady=10, sticky="w")

# "0'a Çevir" Butonu
error_type_0_button = tk.Radiobutton(
    root,
    text="0'a Çevir",
    variable=error_type_var,
    value="0'a Çevir",
    bg=dark_bg,
    fg=light_fg,
    selectcolor=dark_bg,
    state=tk.DISABLED,  # Başlangıçta pasif
)
error_type_0_button.grid(row=5, column=1, padx=5, pady=10, sticky="e")


def validate_error_bit_entry(event):
    """
    Hata Bit Konumu girişinin geçerliliğini doğrular.
    """
    bit_num = error_bit_entry.get()
    if bit_num.strip().isdigit():
        error_type_1_button.config(state=tk.NORMAL)
        error_type_0_button.config(state=tk.NORMAL)
    else:
        error_type_1_button.config(state=tk.DISABLED)
        error_type_0_button.config(state=tk.DISABLED)


# Hata Bit Konumu girişine bağlı olarak kontrol
error_bit_entry.bind("<KeyRelease>", validate_error_bit_entry)


def generate_change_btn_color_enter(event):
    event.widget.config(bg="green")
    root.config(cursor="hand2")


def generate_change_btn_color_leave(event):
    event.widget.config(bg="#006400")
    root.config(cursor="")


# Hamming kodu üretme butonu
generate_code_button = tk.Button(
    root,
    text="Hamming Kodu Üret",
    command=generate_hamming_code,
    bg="#006400",
    fg=light_fg,
)
generate_code_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
generate_code_button.config(state=tk.DISABLED)
generate_code_button.bind("<Enter>", generate_change_btn_color_enter)
generate_code_button.bind("<Leave>", generate_change_btn_color_leave)


def error_change_btn_color_enter(event):
    event.widget.config(bg="#a5002a")
    root.config(cursor="hand2")


def error_change_btn_color_leave(event):
    event.widget.config(bg="#A52A2A")
    root.config(cursor="")


# Hata oluşturma butonu
introduce_error_button = tk.Button(
    root,
    text="Hata Oluştur",
    command=introduce_error,
    bg="#A52A2A",
    fg=light_fg,
)
introduce_error_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
introduce_error_button.config(state=tk.DISABLED)  # Başlangıçta devre dışı bırakıldı
introduce_error_button.bind("<Enter>", error_change_btn_color_enter)
introduce_error_button.bind("<Leave>", error_change_btn_color_leave)


def detect_change_btn_color_enter(event):
    event.widget.config(bg="#0000cd")
    root.config(cursor="hand2")


def detect_change_btn_color_leave(event):
    event.widget.config(bg=button_bg)
    root.config(cursor="")


# Hata tespit ve düzeltme butonu
detect_and_correct_button = tk.Button(
    root,
    text="Hata Tespit et ve Düzelt",
    command=detect_and_correct_error,
    bg=button_bg,
    fg=light_fg,
)
detect_and_correct_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
detect_and_correct_button.config(state=tk.DISABLED)  # Başlangıçta devre dışı bırakıldı
detect_and_correct_button.bind("<Enter>", detect_change_btn_color_enter)
detect_and_correct_button.bind("<Leave>", detect_change_btn_color_leave)

info_text = tk.Label(
    root,
    text="© 2024 Hamming Error-Correcting Code Simülatörü",
    bg=dark_bg,
    fg=light_fg,
)
info_text.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

if __name__ == "__main__":
    # Pencere ayarları
    root.protocol("WM_DELETE_WINDOW", on_closing)

# Pencere ayarları
root.protocol("WM_DELETE_WINDOW", on_closing)

# Tkinter döngüsünü başlat
root.mainloop()
