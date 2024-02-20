# Hi! This is code of KosmoNews site! U can use this code to make your own site
## Instruction for insalling
### Linux:
requires: 
- [git](https://git-scm.com/download/linux)
- [python 3.11](https://www.scaler.com/topics/python/install-python-on-linux/)

Open terminal. Paste these commands:
```bash
git clone https://github.com/donko1/KosmoNews.git
```
```bash
cd KosmoNews
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python3 manage.py runserver
```
#### If u want use test DataBase:
```bash
cp exampleDB/db.sqlite3 .
``` 
### Windows:
requires:
- [git](https://git-scm.com/download/win)
- [python 3.11](https://python.org)


Open terminal(<kbd>WIN</kbd> + <kbd>R</kbd>. In window paste `cmd` and press <kbd>ENTER</kbd>). Paste these commands:
```bash
git clone https://github.com/donko1/KosmoNews.git
```
```bash
cd KosmoNews
```
```bash
python -m venv venv
```
```bash
.\venv\Scripts\activate
```
```
pip install -r requirements.txt
```
```bash
python manage.py runserver
```
#### If u want use test DataBase:
```bash
copy exampleDB/db.sqlite3 .
```
