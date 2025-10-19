# Termux-SEfile (Security Encryption file)

[![Python](https://img.shields.io/badge/Dil-Python-blue)](https://www.python.org/)
[![Lisans](https://img.shields.io/badge/Lisans-GPLv3-red)](LICENSE)
[![Durum](https://img.shields.io/badge/Aşama-Beta-orange)](##Proje-Durumu)

**"Termux için shell script ile yazılmış, python tabanlı dosya şifreleme ve çözme aracıdır (Security Encryption file)."**

---

## 🚀 Proje Durumu ve Kurulum

### Aşama: Beta (Deneme Sürümü)

Bu proje şu anda Beta aşamasındadır. Temel şifreleme ve çözme fonksiyonları çalışmaktadır, ancak yeni özellikler eklenecek ve kapsamlı testler devam edecektir.

### Kurulum (Termux)

Gerekli paketleri Termux'a kurarak başlayın:

1.  **Gerekli Paketleri Kurun:**
    ```bash
    pkg install python git
    pip install pycryptodome
    ```

2.  **Depoyu Klonlayın ve Çalıştırın:**
    ```bash
    git clone [https://github.com/YigitMehmet-KidEthicalHacker/Termux-SEfile.git](https://github.com/YigitMehmet-KidEthicalHacker/Termux-SEfile.git)
    cd Termux-SEfile
    python SEfile.py
    ```
    *(Not: `git clone` komutundaki kullanıcı adını kendi GitHub kullanıcı adınızla değiştirin.)*

## 💡 Sorunlar, Riskler ve Testler

### Bilinen Sorunlar
* **Termux Bağımlılık Hataları:** Shell script versiyonunda `openssl` komutunun sistem yolunda (PATH) bulunamaması gibi nadir sistem sorunları gözlemlenmiştir. Python sürümü bu sorunları aşmak için tasarlanmıştır.
* **Hata Yakalama:** Kodun genel hata yakalama mekanizmaları (try-except blokları) genişletilecektir.

### Veri Kaybı Riski
* **Risk:** Şifreleme algoritması (AES-256-CBC) güvenlidir. Ancak, şifreleme/çözme işlemi sırasında cihazın aniden kapanması veya şarjının bitmesi gibi durumlar, her programda olduğu gibi, işlemdeki dosyanın bozulmasına **NEDEN OLABİLİR**.
* **Öneri:** Lütfen önemli dosyalarınızın yedeğini almadan kullanmayınız.

### Test Durumu
* Kod, geliştirici tarafından temel şifreleme ve çözme işlevleri açısından başarıyla test edilmiştir.

---

## ⚖️ SORUMLULUK REDDİ BEYÂNI (DISCLAIMER)

BU KOD VE PROJE **HALA DENEME AŞAMASINDADIR (BETA)**.

**YAPIMCI (Yiğit Mehmet), BU KODUN KULLANIMINDAN KAYNAKLANABİLECEK HERHANGİ BİR VERİ KAYBINDAN, HASARDAN VEYA MADDİ/MANEVİ ZARARDAN KESİNLİKLE VE ASLA SORUMLU DEĞİLDİR.**

* Bu araç, geliştiricisi tarafından sadece 1 kez temel fonksiyonları açısından test edilmiştir.
* Tüm risk kullanıcıya aittir.

Bu proje, **GNU Genel Kamu Lisansı v3.0 (GPLv3)** ile korunmaktadır. Bu, kodu kullanabileceğiniz, değiştirebileceğiniz ve paylaşabileceğiniz anlamına gelir, ancak tüm değişikliklerinizin de aynı lisans altında olması gerekir.
