# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:12:02 2023

@author: Excalibur
"""

# paket içe aktarma
from flask import Flask, render_template


# flask uygulama oluşturma başlatma
app = Flask(__name__)

# / yolu için rota belirleme ve istekleri işleme
@app.route('/')
def anasayfa():
    # tarayıcıda görüntülenecek içerik
    return render_template("index.html")

# proje çalıştırıldıysa
if __name__ == '__main__':
    # uygulamayı debug modunda çalıştır
    app.run(debug=True)
    
"""

http://localhost:5000
    
 * Serving Flask app 'flaskilkproje' # proje adı
 * Debug mode: on # debug mod başlatıldı
 # başlatma ile alaklı açıklama yazısı
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    # tarayıcya girip bize verdiği adresi girmemizi istediği adres
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

"""


"""

TARİHÇE:
    
    
RESTful API (Representational State Transferful API), uygulama programlama arayüzlerini 
(API) tasarlamak ve uygulamak için kullanılan bir yaklaşım ve bir mimari stilidir. REST,
 Roy Fielding tarafından 2000 yılında doktora tezi olarak tanımlanan bir mimaridir. RESTful API, 
 bu REST prensiplerini takip eden bir API anlamına gelir.

İşte RESTful API'nin temel prensipleri:

Kaynaklar (Resources): Her şey bir kaynaktır (resource). Örneğin, 
bir blog uygulamasında makaleler, yorumlar, kullanıcılar vs. her biri birer
 kaynaktır.

Temsil Durumu (Representation): Kaynaklar, temsil durumuyla (representation) ifade edilir. 
Bu, JSON, XML veya başka bir formatta olabilir. Bir kaynağın durumu, kullanıcıya sunulan temsil
 ile iletişim kurar.

Stateless (Durumsuz): Her istek, isteği yapan tarafından tüm bilgiyi içermelidir. Sunucu durumu 
(state) tutmaz. İstekler arasında durumu saklamak için oturum (session) kullanılmaz.

Birleşik Arayüz (Uniform Interface): RESTful servislerin birleşik ve basit bir arayüzü vardır.
 Bu arayüz, aynı prensiplere uygun olan bir dizi standart operasyon içerir. Bu operasyonlar, kaynaklara erişim, 
 temsil durumu alma ve temsil durumu gönderme gibi işlemleri içerir.

HATEOAS (Hypertext As The Engine Of Application State): Bu prensip, uygulama durumunu yönlendirmek
 için hipertext kullanılmasını ifade eder. İstemci, servisin nasıl kullanılacağına dair bilgileri temsil durumu 
 içindeki bağlantılardan (links) alır.

Katmanlılık (Layered System): Bu prensip, mimarinin katmanlı olmasını ifade eder. Her katmanın belirli bir 
sorumluluğu vardır ve bir katman, yalnızca altındaki katmanla doğrudan etkileşimde bulunur.

RESTful API'ler, HTTP protokolünü kullanarak genellikle CRUD (Create, Read, Update, Delete) operasyonlarını destekler.
 HTTP metodları (GET, POST, PUT, DELETE vb.) kullanılarak kaynaklar üzerindeki işlemler gerçekleştirilir. RESTful API'ler,
 özellikle web tabanlı uygulamalarda ve mikroservis mimarilerinde yaygın olarak kullanılır.

"""



