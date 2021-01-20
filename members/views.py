from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
# Create your views here.
def gu(req):
    num = req.GET.get('num', '')
    return HttpResponse(f'<h1>gugu : {num_gugu(num)}</h1>')

def num_gugu(num):
    str = ""
    for i in range(1,10):
        str += f'{int(num)} * {i} = {int(num) * i}<br>'
    return str    

def index(request):
    return HttpResponse("<h1>Wonderful World</h1>")

def test(req):
    return HttpResponse("<h2>Test</h2>")

def test2(req):
    return HttpResponse("<h2>Test2</h2>")

def git(req):
    return HttpResponse("visual code 이용한 git사용")

def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        #if username == 'exit':
        #    return HttpResponse('나가기')
        #elif username == 'codingon':
        #    return render(req, 'login.html')
        member = Members(
                username = username,
                useremail = email
        )
       
        member.save()
        res_data = {}
        res_data['res'] = '등록성공'
        return render(req, 'index.html', res_data)
    
    return render(req, 'index.html')
def calender(req):
    return render(req, 'cal.html', {})
