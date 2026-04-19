import tf_keras as keras  
from tf_keras.models import load_model  
from PIL import Image, ImageOps  
import time

np.set_printoptions(suppress=True)

model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
image = Image.open("/img/images.jpeg").convert("RGB")

size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
data[0] = normalized_image_array

prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

print("\n" + "="*50)
print("🌍 ПРИРОДНОЕ ЯВЛЕНИЕ 🌍")
print("="*50)
print("Class:", class_name[2:].strip())
print(f"Уверенность: {confidence_score:.2%}")
print("="*50)
print("📖 Описание:\n")
time.sleep(3)

if class_name[2:].strip() == ("Лесные пожары"):
  print("🔥 Лесной пожар — это неконтролируемое горение растительности,\nстихийно распространяющееся по лесной территории.\n")
  print("📌 В 88–98% случаев причинами становятся:\n- человеческий фактор (неосторожность, палы травы)\n- лишь в 2–12% — природные факторы (молнии)\n")
  print("📌 Основные виды:\n- низовые (горят подстилка, трава)\n- верховые (горят кроны)\n- торфяные.")

if class_name[2:].strip() == ("Засуха"):
  print("🏜️ Засуха — это опасное природное явление,\nхарактеризующееся продолжительным отсутствием или\nнезначительным количеством осадков.\n")
  print("📌 Сопровождается:\n- высокой температурой\n- низкой влажностью воздуха\n")
  print("📌 Последствия:\n- дефицит воды\n- нарушение водного баланса растений\n- гибель урожая\n- серьезный ущерб сельскому хозяйству")

if class_name[2:].strip() == ("Таяние льда"):
  print("🧊 Таяние льда — это физический процесс перехода воды\nиз твердого состояния в жидкое (плавление),\nпроисходящий при нагревании выше 0°C.\n")
  print("📌 Особенности:\n- природное явление, характерное для весны (ледоход)\n- следствие глобального потепления\n")
  print("📌 Последствия:\n- сокращение ледников\n- подъем уровня моря")

if class_name[2:].strip() == ("Наводнение"):
  print("🌊 Наводнение — это временное затопление\nзначительной части суши водой.\n")
  print("📌 Причины:\n- природные факторы (паводки, половодье, заторы льда, сильные дожди)\n- разрушение гидротехнических сооружений (плотин, дамб)\n")
  print("📌 Последствия:\n- ущерб инфраструктуре\n- затопление населенных пунктов\n- опасность для жизни людей")

print("\n" + "="*50)
print("✅ Готово!")
#необходимые библиотеки: tf-keras pillow numpy
#установка: pip install tf-keras pillow numpy