import openai

# OpenAI API Anahtarınızı burada belirtin
openai.api_key = "API KEY YAPISTIRMA ALANI"

# GPT-3'ün hangi model ve engine ile çalışacağını belirtin
model_engine="text-davinci-003"

# OpenAI API'ye istek yapmak için completion adlı bir değişken olusturduk
#engine,prompt,temperature parametrelerimimi belirledik
while True:
    prompt = input("Soru veya mesajınızı yazın: ")
    if prompt.lower() == "exit":
        break
    
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.4,
        max_tokens=1024,
        n=1,
        stop=None,
        )
# İstekten gelen cevabı response değişkenine aktaralım
    response = completion.choices[0].text
    
# Cevabı ekrana yazdıralım
    print(response)