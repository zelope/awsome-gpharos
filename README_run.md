
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
settings.py는  config 폴더 안에 넣고
.config는 manage.py랑 같은 계층에 두기

### step2
```powershell
python manage.py makemigrations      
```

### step3
```powershell
python manage.py migrate          
```

## 1-3. (로컬에서) 실행
### step1
```powershell
python manage.py runserver    
```

### step2 : 신호 전송 및 hotplace 화면 실행
카톡 주세요 ! (데이터 I/O 마다 비용이 들어서 평소에는 꺼둠....)
