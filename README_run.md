
(powershell = cmd = bash)
git clone한 폴더에서 다음 작업 수행
지난번에 했을 때 형 powershell이 외부권한 접근 불가라 git cmd에서 git clone 되어있는 폴더 접근해서
아래 내용들 실행해야 할듯

## 1-1. 가상환경 설정
### step1
```powershell
py -3.11 -m venv .venv
```
### step2
```powershell
.\.venv\Scripts\activate      
```

### step3
```powershell
py -m pip install --upgrade pip     
```

### step4
```powershell
pip install -r requirements.txt  
```

## 1-2. setting file
### step1
내가 보낸 파일을 config 폴더 안에 넣기

### step2
```powershell
python manage.py makemigrations      
```

### step3
```powershell
python manage.py migrate          
```

## 1-3. (로컬에서) 실행
```powershell
python manage.py runserver    
```
