# ChatGPT-ile-Sohbet

terminalden yükleme yapın:
pip install openai 

https://chat.openai.com/auth/login sitesinden giris yapın ve APIKEY olusturun
Bu APIKEY i ilgili satıra yapıstırın

Kullanılan parametreler nedir ne anlama gelir?
engine: OpenAI tarafından sunulan farklı dil yapay zeka modellerinden birini belirtmek için kullanılan bir parametredir. Bu modele göre, modelin verimliliği ve performansı değişebilir. Örneğin, "davinci" engine'i, dil yapay zekası modelleri arasında en yüksek doğruluğu ve başarıyı sağlar.

prompt: Modelin kullanacağı ana metin, soru veya görevi tanımlamak için kullanılan bir parametredir. OpenAI API, modelin görevin ne olduğunu belirlemesine ve bu göreve göre cevap üretmesine yardımcı olacak bir dizi anahtar kelime veya cümleler sağlamak için kullanılabilir.

temperature: Temperature, modelin öngörülen çıktısının tutarlılığını belirleyen bir parametredir. Temperature, modelin ne kadar riskli veya yaratıcı olabileceğini belirler. Yüksek bir temperature, modelin daha yaratıcı olmasına ve daha düşük bir temperature daha güvenilir yanıtlar üretmesine neden olur.

Bu parametre 0 ile 1 arasında bir değer alır ve genellikle 0.5 ile 0.9 arasında seçilir.
