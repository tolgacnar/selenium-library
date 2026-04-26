# 🤖 Instagram Otomasyon Botu — Selenium Web Scraping

Instagram üzerinde **giriş yapma**, **takipçi listesini çekme**, **kullanıcı takip etme** ve **takipten çıkma** işlemlerini otomatikleştiren bir Python + Selenium projesi.

---

## 📑 İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Selenium ve Web Scraping Nedir?](#selenium-ve-web-scraping-nedir)
- [Proje Yapısı](#proje-yapısı)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Kod Açıklaması](#kod-açıklaması)
- [Güvenlik Uyarıları](#güvenlik-uyarıları)
- [Yasal Uyarı](#yasal-uyarı)

---

## 📖 Proje Hakkında

Bu proje, Selenium kütüphanesi kullanarak Instagram web sitesi üzerinde otomatik işlemler gerçekleştiren bir Python botudur. Temel amacı:

- Instagram hesabına otomatik giriş yapmak
- Hesaptaki tüm takipçileri listelemek ve `followers.txt` dosyasına kaydetmek
- Belirli kullanıcıları takip etmek veya takipten çıkmak

---

## 🌐 Selenium ve Web Scraping Nedir?

### Web Scraping

**Web scraping**, web sitelerinden otomatik olarak veri toplama işlemidir. Bir web tarayıcısının yaptığı işlemleri (sayfa açma, butona tıklama, metin okuma vb.) programatik olarak gerçekleştirir. Kullanım alanları:

- Veri toplama ve analiz
- Sosyal medya otomasyonu
- Fiyat karşılaştırma
- İçerik izleme

### Selenium

**Selenium**, web tarayıcılarını otomatize etmek için kullanılan açık kaynaklı bir araçtır. Gerçek bir tarayıcıyı (Chrome, Firefox vb.) programatik olarak kontrol etmenizi sağlar.

#### Selenium'un Temel Bileşenleri

| Bileşen | Açıklama |
|---------|----------|
| `webdriver.Chrome()` | Chrome tarayıcısını başlatır ve kontrol eder |
| `find_element()` | Sayfadaki HTML elementlerini bulur (XPath, CSS Selector, ID vb.) |
| `send_keys()` | Bir input alanına metin girer |
| `.click()` | Bir elemente tıklar |
| `WebDriverWait` | Belirli bir elementin yüklenmesini bekler (explicit wait) |
| `expected_conditions` | Bekleme koşullarını tanımlar (element görünür mü, tıklanabilir mi vb.) |
| `execute_script()` | JavaScript kodunu doğrudan tarayıcıda çalıştırır |

#### Element Bulma Yöntemleri

```python
# XPath ile bulma — en esnek yöntem
browser.find_element(By.XPATH, "//div[@role='dialog']")

# Tag adı ile bulma
browser.find_element(By.TAG_NAME, "button")

# Metin içeriğine göre bulma (XPath contains)
browser.find_element(By.XPATH, "//span[contains(text(), 'takipçi')]")

# Href içeriğine göre bulma
browser.find_element(By.XPATH, "//a[contains(@href, '/followers')]")
```

#### Bekleme (Wait) Mekanizmaları

Selenium'da iki tür bekleme vardır:

1. **Implicit Wait (Örtülü Bekleme):** `time.sleep(saniye)` — Sabit süre bekler. Basit ama verimsizdir.
2. **Explicit Wait (Açık Bekleme):** `WebDriverWait` — Belirli bir koşul sağlanana kadar bekler. Daha verimlidir.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(browser, 15)  # Maksimum 15 saniye bekle

# Element sayfada var olana kadar bekle
wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))

# Element tıklanabilir olana kadar bekle
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers')]")))
```

---

## 📁 Proje Yapısı

```
cursorss/
├── installing.py        # Ana bot dosyası — tüm otomasyon mantığı burada
├── userinfo.py          # Kullanıcı adı ve şifre bilgileri (⚠️ .gitignore'a ekleyin!)
├── followers.txt        # Çekilen takipçi listesi (otomatik oluşturulur)
├── README.md            # Bu dosya
├── SELENIUM/
│   ├── chromedriver.exe # Chrome tarayıcı sürücüsü
│   └── denem.py         # Undetected ChromeDriver test dosyası
└── __pycache__/         # Python önbellek dosyaları
```

---

## ⚙️ Kurulum

### 1. Gereksinimler

- **Python 3.8+**
- **Google Chrome** tarayıcısı
- **ChromeDriver** (Chrome sürümünüze uygun olmalı)

### 2. Kütüphanelerin Yüklenmesi

```bash
pip install selenium
pip install undetected-chromedriver   # Opsiyonel — bot tespitinden kaçınmak için
```

### 3. Kullanıcı Bilgilerini Ayarlama

`userinfo.py` dosyasını düzenleyerek kendi Instagram bilgilerinizi girin:

```python
username = "instagram_kullanici_adiniz"
password = "instagram_sifreniz"
```

### 4. ChromeDriver

ChromeDriver'ın sisteminizde yüklü olduğundan ve Chrome sürümünüzle uyumlu olduğundan emin olun. İndir: [ChromeDriver İndirme Sayfası](https://chromedriver.chromium.org/downloads)

---

## 🚀 Kullanım

### Takipçi Listesini Çekme

```bash
python installing.py
```

Bu komut:
1. Chrome tarayıcısını açar
2. Instagram'a giriş yapar
3. Profil sayfanıza gider
4. Takipçi diyalog penceresini açar
5. Tüm takipçileri scroll ederek toplar
6. Sonuçları `followers.txt` dosyasına kaydeder

### Kullanıcı Takip Etme / Takipten Çıkma

`installing.py` dosyasındaki ilgili satırları yorum işaretinden çıkararak kullanabilirsiniz:

```python
# Takip etme
github.followuser("kullanici_adi")

# Takipten çıkma
github.unfollowuser("kullanici_adi")
```

---

## 🔍 Kod Açıklaması

### `GitHub` Sınıfı (Ana Bot Sınıfı)

> **Not:** Sınıf adı `GitHub` olarak kalmış olsa da, bu bot Instagram için tasarlanmıştır.

#### `__init__(self, username, password)`
Tarayıcıyı başlatır ve kullanıcı bilgilerini saklar.

```python
def __init__(self, username, password):
    self.browser = webdriver.Chrome()   # Chrome tarayıcısını aç
    self.username = username
    self.password = password
```

#### `signIn(self)` — Giriş Yapma
Instagram giriş sayfasını açar, kullanıcı adı ve şifreyi XPath ile bulunan input alanlarına girer, ardından giriş butonuna tıklar.

**Kullanılan Selenium teknikleri:**
- `browser.get(url)` — Sayfaya git
- `find_element("xpath", ...)` — XPath ile element bul
- `send_keys(text)` — Metin gir
- `.click()` — Butona tıkla

#### `getFollowers(self)` — Takipçi Çekme
Bu fonksiyon en karmaşık bölümdür ve birçok Selenium tekniğini bir arada kullanır:

1. **Profil sayfasına gitme** ve sayfanın yüklenmesini bekleme (`WebDriverWait`)
2. **Takipçi sayısını okuma** — `contains(text(), 'takipçi')` XPath ifadesi ile
3. **Takipçi diyaloğunu açma** — `execute_script()` ile JavaScript click
4. **Scroll ile tüm takipçileri toplama** — `scrollTop = scrollHeight` JavaScript komutu ile diyaloğu aşağı kaydırma
5. **Tekrarlanan linkleri filtreleme** — `/explore`, `/p/`, `/reel/` gibi ilgisiz linkleri hariç tutma
6. **Dosyaya kaydetme** — Toplanan tüm takipçi URL'lerini `followers.txt` dosyasına yazma

```python
# Diyaloğu scroll etme — JavaScript ile
self.browser.execute_script(
    "arguments[0].scrollTop = arguments[0].scrollHeight", dialog
)
```

#### `followuser(self, username)` — Takip Etme
Kullanıcı profiline gider, "Following" yazan butonu bulursa tıklar.

#### `unfollowuser(self, username)` — Takipten Çıkma
Kullanıcı profiline gider, "Following" yazmayan butonu bulursa tıklar ve ardından onay diyaloğundaki "Takibi bırak" butonuna tıklar.

---

## 🛡️ Güvenlik Uyarıları

> [!CAUTION]
> **`userinfo.py` dosyanızda şifreniz düz metin olarak saklanmaktadır!**

### Yapmanız Gerekenler:

1. **`.gitignore` dosyası oluşturun** ve hassas dosyaları ekleyin:

```
# .gitignore
userinfo.py
followers.txt
__pycache__/
*.exe
```

2. **Ortam değişkenleri kullanın** (önerilen yöntem):

```python
import os

username = os.environ.get("INSTAGRAM_USERNAME")
password = os.environ.get("INSTAGRAM_PASSWORD")
```

3. Bu projeyi **asla şifrelerinizle birlikte GitHub'a yüklemeyin**.

---

## ⚖️ Yasal Uyarı

> [!WARNING]
> Bu proje yalnızca **eğitim amaçlıdır**. Instagram'ın Kullanım Koşulları, otomatik botların ve scraping araçlarının kullanımını yasaklamaktadır. Bu aracın kullanımından doğabilecek hesap kısıtlamaları veya yasal sorunlardan kullanıcı sorumludur.

---

## 📚 Faydalı Kaynaklar

| Kaynak | Link |
|--------|------|
| Selenium Resmi Dokümantasyon | [selenium.dev/documentation](https://www.selenium.dev/documentation/) |
| Selenium Python Bindings | [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/) |
| ChromeDriver İndirme | [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) |
| XPath Rehberi | [w3schools.com/xml/xpath_intro](https://www.w3schools.com/xml/xpath_intro.asp) |

---

<p align="center">
  <b>Python 🐍 + Selenium 🌐 ile geliştirilmiştir</b>
</p>
