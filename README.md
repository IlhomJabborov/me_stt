# me_stt
STT Model.

## Ishlatish
* Git clone yoki to'g'ridan to'g'ri faylni yuklab oling.
* Paketlarni o'rnatish :
  ```
  pip install -r requirements.txt
  ```
* Yoki :
  ```
  pip install transformers torchaudio
  ```
* STT Modelni quydagi manzildan yuklab oling :
  ```
  Bu yerda model manzili bo'ladi
  ```
* Model [ my_stt.zip ] shaklida yuklanadi.Faylni zipdan chiqarib,asosiy loyiha fayliga qo'shing.
* Umumiy fayl strukturasi quydagicha ko'rinishda bo'lishi kerak :
   <img src="Screenshot 2024-11-14 200439.png" alt="struktura file" style="height: 150px; width:70%;"/>
* [ main.py ] faylida yozilgan kodning quydagi qismiga audio manzilini(audio path) kiriting :
  ```
  audio_p = "8703.wav"  # Path almashtiring
  ```
* Dasturni ishlatish :
  ```
  python main.py
  ```
## Natija 
Siz kiritgan audio text ko'rinishida chop etiladi :
``` bash
STT Natijasi : bu yerda audiodagi matn chiqdi
```

### Qo'shimcha yordam
Audio manzilini(path) topishda muammo chiqsa,quydagi buyruq orqali hal qilinadi :
```
sudo apt-get install sox libsox-dev libsox-fmt-all
```

## 2024
