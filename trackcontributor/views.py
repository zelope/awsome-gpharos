from django.shortcuts import render

def contributor(request):
    
    members = list()
    
    for _ in range(4):
       member = dict()
       member['profile_image'] = "img/no_img.png" 
       member['name'] = '홍길동'
       member['role'] = "수업듣기"
       member['bio'] = "skn"
    
    
    context = {"members" : members}
    return render(request, 'contributor.html',context = context)
