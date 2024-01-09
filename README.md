
Привет! Рекомендуем установить python 3.11 и использовать эти команды:

cd /Полный/Путь/До/Папки

pip install -r requirements.txt

python

import nltk

nltk.download('punkt', quiet=True)
nltk.download("omw-1.4", quiet=True)

quit()

python manage.py runserver