TÜM HAKLARI UWPEAR'A AİTTİR.

# 🔐 Login Bypass otomasyon

Bu Python programı, bir web sitesine bypass kodlarını hızlıca denemek için kullanılır. `passwords.txt` dosyasındaki her şifre hem kullanıcı adı hem de şifre olarak kullanılacaktır. Bu şekilde, aynı değeri kullanıcı adı ve şifre alanlarına girerek doğru kombinasyonu bulmaya çalışır.

## 📋 Özellikler

- Bir web formuna POST isteği gönderir.
- `passwords.txt` dosyasındaki metinleri hem usarname hem de password olarak kullanır.
- Girişlerin doğru olup olmadığını belirlemek için terminalden Yanlış veya Doğru yazısını görürsünüz.
- Başarılı giriş tespit edildiğinde doğru şifreyi konsola yazdırır.

## 🔧 Gereksinimler

- Python 3.x
- `requests` kütüphanesi

## 🚀 Kurulum

1. **Python ve Gereksinimleri Kurun:**

   Python 3.x yüklü değilse [Python'un resmi web sitesinden](https://www.python.org/downloads/) yükleyin.

   `requests` kütüphanesini yüklemek için aşağıdaki komutu çalıştırın:

   ```bash
   pip install requests
   ```

2. **Proje dosyalarını indirin:**
    
    Bu proje dosyalarını bir dizine indirmek için bir terminal açın ve aşağıdaki kodu kopyalayıp terminalinize yapıştırın.
    
    ```bash
    git clone https://github.com/uwpear/bypass-automation
    ```

    passwords.txt Dosyasını Hazırlayın:

    passwords.txt dosyasını oluşturun veya kendi verdiğim dosyayı kullanın. Her satıra bir şifre ekleyin. Şifreler hem kullanıcı adı hem de şifre olarak kullanılacaktır.


🛠️ Kullanım
    Programı Çalıştırın:

    Terminal veya komut istemcisinde, programın bulunduğu dizine gidin ve aşağıdaki komutu çalıştırın:

    ```bash
    python password_tester.py
    Gerekli Bilgileri Girin:
    ```
    Hedef Site: Giriş formunun URL'sini girin.
    
    Sonuçları İnceleyin. İşte bu kadar basit!

    Program, her şifreyi hem kullanıcı adı hem de şifre olarak deneyerek doğru kombinasyonu bulmaya çalışır. Doğru şifre tespit edildiğinde, başarılı giriş mesajı ve doğru şifre konsola yazdırılır.

🖼️ Örnek
    Programı çalıştırdığınızda şu şekilde görünebilir:


Hedef Site (giriş formunun URL'si): https://example.com/login

[ - ] Yanlış Şifre!: 123456
[ - ] Yanlış Şifre!: password
[ + ] Doğru Şifre!: admin

⚠️ ÖNEMLİ
    Bu program sadece kendi hesaplarınızda ve izin verilen sistemlerde kullanılmalıdır. Başka sistemlerde deneme yapmadan önce uygun izinleri aldığınızdan emin olun. YAPILAN HER İLLEGAL AKTİVİTEDE BENİM SORUMLULUĞUM DEĞİL, KULLANICININ KENDİ İRADESİ İLE YAPTIĞI SORUNDUR. O yüzden dikkatli ve legal kullanmaya dikkat edin.

📊 Sonuç
    Web formunun başarılı giriş yanıtını anlamak için doğru yanıt metnini belirlemeniz gerekebilir. 'Giriş başarılı' ifadesini uygun yanıt metniyle değiştirin.

📝 Lisans
    Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz.

📧 İletişim
    Herhangi bir soru veya sorun için byates_41@protonmail.com adresi ile iletişime geçebilirsiniz.
