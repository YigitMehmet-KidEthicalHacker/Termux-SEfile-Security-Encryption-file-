import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

# --- Helper Fonksiyonu: Padding Ekleme ---
def pad(data):
    BLOCK_SIZE = 16
    padding_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([padding_len]) * padding_len

# --- Helper Fonksiyonu: Padding Kaldırma ---
def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

# --- Şifreleme Fonksiyonu ---
def encrypt_file(file_path, output_path, password):
    hasher = SHA256.new(password.encode('utf-8'))
    key = hasher.digest()

    try:
        data = open(file_path, "rb").read()
    except FileNotFoundError:
        print(f"Hata: Giriş dosyası '{file_path}' bulunamadı.")
        sys.exit(1)
        
    padded_data = pad(data)
    
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(padded_data)

    with open(output_path, "wb") as f:
        f.write(cipher.iv)  # IV'yi yaz
        f.write(ciphertext)
    
    print(f"Başarılı! Dosyanız '{output_path}' olarak şifrelendi.")

# --- Çözme Fonksiyonu ---
def decrypt_file(file_path, output_path, password):
    hasher = SHA256.new(password.encode('utf-8'))
    key = hasher.digest()

    try:
        with open(file_path, "rb") as f:
            iv = f.read(16)
            ciphertext = f.read()
    except FileNotFoundError:
        print(f"Hata: Giriş dosyası '{file_path}' bulunamadı.")
        sys.exit(1)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_data = cipher.decrypt(ciphertext)
    
    try:
        data = unpad(decrypted_padded_data)
    except ValueError:
        print("Hata: Şifreleme anahtarı (parola) yanlış veya dosya bozuk.")
        sys.exit(1)

    with open(output_path, "wb") as f:
        f.write(data)

    print(f"Başarılı! Dosyanız '{output_path}' olarak çözüldü.")


# --- Ana Program Bloğu ---
if len(sys.argv) != 4:
    print("Kullanım: python SEfile.py [sec/dec] <Giriş Dosyası> <Çıkış Dosyası>")
    sys.exit(1)

operation = sys.argv[1]
in_file = sys.argv[2]
out_file = sys.argv[3]

if operation == "sec":
    password = input("Dosya şifreleniyor... Parolanızı girin: ")
    encrypt_file(in_file, out_file, password)
elif operation == "dec":
    password = input("Dosyanın şifresi çözülüyor... Parolanızı girin: ")
    decrypt_file(in_file, out_file, password)
else:
    print(f"Geçersiz işlem: '{operation}'. Lütfen 'sec' veya 'dec' kullanın.")
