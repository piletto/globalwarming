# global_warming

# 🌍 Классификатор природных явлений

Простая нейросеть, которая определяет 4 природных явления по фотографии и показывает их описание.

## 📸 Что распознаёт?

| Явление | Эмодзи |
|---------|--------|
| Лесные пожары | 🔥 |
| Засуха | 🏜️ |
| Таяние льда | 🧊 |
| Наводнение | 🌊 |

## 📁 Файлы для работы

global_warming/
├── keras_model.h5 ← обученная нейросеть
├── labels.txt ← названия классов
├── predict.py ← твой скрипт
└── image.jpg ← твоё фото


## 🛠️ Установка

### Открой терминал и выполни:

### pip install tf-keras pillow numpy

## 🚀 Запуск
### 1. Помести в папку файлы keras_model.h5 и labels.txt

### 2. Замени в коде путь к фото:
   ### image = ImageOpen("путь_к_твоему_фото.jpg")

## 📺 Что увидишь на экране?
### (пример)

### ==================================================
### 🌍 ПРИРОДНОЕ ЯВЛЕНИЕ 🌍
### ==================================================
### Class: Лесные пожары
### Уверенность: 98.45%
### ==================================================
### 📖 Описание:

### 🔥 Лесной пожар — это неконтролируемое горение...
### (и дальше красивое описание)
### ==================================================
### ✅ Готово!





## Я использовала компьютерное зрение －O－
#### Я пользовалась ресурсами из модуля 6.


## Библиотеки, которые я использовала
- Библиотеки:
> tf-keras==2.15.0
> pillow==10.0.0
numpy==1.24.3
fastapi==0.63.0
uvicorn==0.12.2

## Референсы, которые мне пригодились (мои)
- Референсы:
> https://colab.research.google.com/drive/1ZvLMa59UbmXg9QLpsGAAZRiRVWkM91I4?usp=sharing
> https://colab.research.google.com/drive/1Ktz9nm_m9bCxPc9QiXETy71iEV6kDgwE?usp=sharing

## Гайды-статьи, где есть полезная для меня информация
- Лесные пожары: https://73.mchs.gov.ru/deyatelnost/poleznaya-informaciya/rekomendacii-naseleniyu/lesnoy-pozhar-prichiny-vozniknoveniya-i-pravila-povedeniya-pri-obnaruzhenii
- Засуха: https://25.mchs.gov.ru/deyatelnost/poleznaya-informaciya/rekomendacii-naseleniyu/chs-prirodnogo-haraktera/zasuha
- Таяние льдов: https://science.mail.ru/articles/6365-tayanie-lednikov/
- Наводнение: https://92.mchs.gov.ru/deyatelnost/poleznaya-informaciya/rekomendacii-naseleniyu/proisshestviya-prirodnogo-haraktera/navodnenie

