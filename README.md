# Hi! This is code of KosmoNews site! U can use this code to make your own site
## Instruction for insalling
### Linux:
requires: 
- git
- python 3.11
```bash
git clone https://github.com/donko1/KosmoNews.git
```
```bash
cd KosmoNews
```
```bash
cp exampleDB/db.sqlite3 .
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
### Windows:
requires:
- git
- python 3.11
```bash
git clone https://github.com/donko1/KosmoNews.git
```
```bash
cd KosmoNews
```
```bash
copy exampleDB/db.sqlite3 .
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
python3 manage.py runserver
```
