### 1. html파일은 templates 안에 있어야 적용됨
### 2. 만약, css 나 js 나 img 파일을 가져오고 싶을 때는, static 하위 폴더부터 적으면 된다링
### 3. folium 객체는 folium.Map._repr_html_()를 통해, html 객체로 전송

## 데이터 구조 (template 기준)

### includes/sidebar.html
- 사이드바를 정의하는 html. 
- href="{% url 'map-view' %}" 같이 href = 뒤에 있는건 건드리면 안되용

### map.html
#### 메인, 즉 위치추적 화면 
```python
context = {
        'map': m,
        'log_datas' : gps_log[1:],
        "name": gps_data.get("UserName") #str
    }
```
- map : folim 객체 (지도)
- log_datas : 위치 로그 데이터 
```python
gps_log = [ log_dict : dict() ] #형태
```
- - log_dict()
```python
log_dict["Date"] = gps_data.get('Date', 0) #연월일
log_dict["Time"] = gps_data.get('Time', 0) #시분초
log_dict["kor_time"] = log_dict["Time"].strftime("%p %I시 %M분 %S초").replace('AM', '오전').replace('PM', '오후') #한국어로 변경
log_dict["admcode"] = admcode #주소, str
log_dict["addr"] = addr, #주소, str
```

### trackplace/hot.html
#### 주위 ***다수의*** hotplace 들 보여주는 화면

```python
context = {
            "user" : user_data,
            "culture_walk" : send_cw,  
            "leisure" : send_le,
            
        }
```
 - user_data
 ```python
 {"name" : gps_data.get('UserName'), #str
 "location" : legal_str  #주소 str
 }
``` 
 - culture_walk & leisure
 ```python
 {"id" : str(data.id), #str
 "hot_name" : data.fclty_nm, #장소이름 str
 "img_path" : folium 객체 또는 이미지 주속(str)
 } 
``` 

### trackplace/place.html
#### 선택한 place의 세부정보 보여주는 화면 

```python
context = {
        'festival': result,
        'img_path': map #folium 객체
    }
```
 - result
 ```python
result = {
            "festival_name" : deatail_data[0].fclty_nm, #hotplace 이름, str
            "location" : deatail_data[0].adr_nm, #주소, str
            "distance" :distance #거리, km, float,
            "tag" : deatail_data[0].mlsfc_nm #hotplace 종류,
            "blog" : blog_data = list(data)
            
        }
``` 
 - blog_data
 ```python
 {"name" : 블로그 제목, #str
 "url" : 블로그 링크, #장소이름 str
 
 } 
``` 