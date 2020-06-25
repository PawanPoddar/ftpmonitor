
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime, date
from .models import Folder,Files,auth
import ftputil
import json
import time
from django.contrib import messages
from django.contrib.auth.models import User,auth
from myapp.models import Genre



@csrf_exempt
def index(request):
    # # ----------------------------
    # #     h = ftputil.FTPHost("ftp.fi.debian.org", "anonymous", "")
        h = ftputil.FTPHost("localhost",'hello', '12345')
        r = h.walk('/', topdown=True, onerror=None)
        all_list = []
        plist = []
        start = time.time()
        for root, dirs, files in r:
            if root == '/':
                root = ''
            for name in files:
                d = {}
                d['name'] = name
                if not root:
                    d['path'] = '/'
                else:
                    d['path'] = root
                    plist.append(root)
                d['time'] = int(h.stat(root + '/' + name).st_mtime)
                d['size'] = int(h.stat(root + '/' + name).st_size)
                all_list.append(d)
        print(time.time() - start)

        # ----------Insert Data into DB
        dirlist = list(dict.fromkeys(plist))
    #     global new_node
    #     global instance
    #     global parent
        for ml in range(len(dirlist)):
            
    #
            dr = dirlist[ml].split("/")
            dr.remove('', )
            # 1/2/3/4           p-1 c-2/
            for ld in range(len(dr)-1):
            #     parent = Genre.objects.create(name=dr[ld])
            #     Genre.objects.create(name=dr[ld+1], parent=parent)
               check = Folder.objects.filter(name=dr[ld])
               if not check:
                if len(dr) == 1:
                    new_node = Folder(name=dr[0], folder_date=date.today())
                    new_node.save()
                else:
                    y=len(dr)
                    for x in range(ld,y):
                        find = Folder.objects.filter(name=dr[x])
                        if not find:
                            if x != 0:
                                a = x - 1
                                parent = Folder.objects.get(name=dr[a])
                                new_node = Folder(name=dr[x], folder_date=date.today())
                                new_node.insert_at(parent, position="last-child", save=True)
                            else:
                                # x == 0
                                new_node = Folder(name=dr[x], folder_date=date.today())
                                new_node.save()


                for al in all_list:
                    tm=""
                    dat=""
                    if al['path'] == dirlist[ml]:
                        get_time=al['time']
                        dat = datetime.fromtimestamp(get_time)
                        d_ate = dat.strftime("%Y-%m-%d")
                        t_me = dat.strftime("%H:%M:%S")
                        b = Files(folder=new_node, file_name=al['name'],folder_name=dr[ld],size=al['size'], file_date=d_ate,file_time=t_me)
                        b.save()


        return render(request, 'ftpmonitor/index.html', dic)


        # ---------------------------------------------------------------




def allabout(request):
    folder_name=request.GET.get('f_name')
    print(folder_name)
    if not folder_name:
        return JsonResponse({'status':'no folder given'})
    # folder_name="array"
    folder=Folder.objects.filter(name__iexact=folder_name)
    files=folder[0].get_all_files()

    l=[]
    for f in files:
        d = {}
        d['name']=f.file_name
        d['date']=f.file_date
        d['time']=f.file_time
        d['status']=f.file_status
        d['check']=f.check
        d['size']=f.size
        l.append(d)
    return  JsonResponse({"data":l})

def realTime(request):
    folder_name = request.GET.get('f_name')
    if not folder_name:
        return JsonResponse({'status': 'no folder given'})
    h = ftputil.FTPHost("localhost", 'kumar', '12345')
    r = h.walk('/', topdown=True, onerror=None)
    all_list = []
    plist = []
    for root, dirs, files in r:
        if root == '/':
            root = ''
        for name in files:
            d = {}
            d['name'] = name
            if not root:
                d['path'] = '/'
            else:
                d['path'] = root
                plist.append(root)
            d['time'] = int(h.stat(root + '/' + name).st_mtime)
            d['size'] = int(h.stat(root + '/' + name).st_size)
            all_list.append(d)
    mylist = list(dict.fromkeys(plist))
    l=[]
    for ml in range(len(mylist)):
        dr = mylist[ml].split("/")
        dr.remove('', )
        if dr[len(dr) - 1] == folder_name:
            for al in all_list:
                if al['path'] == mylist[ml]:
                    d = {}
                    d['name'] = al['name']
                    d['path'] = al['path']
                    dt = datetime.fromtimestamp(int(al['time']))
                    d['time']= dt
                    d['size']=al['size']
                    l.append(d)
    return JsonResponse({"data": l})

def fileSearch(request):
    file_name = request.GET.get('file_name')
    if not file_name:
        return JsonResponse({'status': 'no folder given'})
    ex=Files.objects.values('file_name','folder_name','file_date','file_time','file_status','check','size').filter(file_name__iexact=file_name)
    l = []
    for f in ex:
        d = {}
        d['name'] = f['file_name']
        d['folder']=f['folder_name']
        d['date'] = f['file_date']
        d['time'] = f['file_time']
        d['status'] = f['file_status']
        d['check'] = f['check']
        d['size'] = f['size']
        l.append(d)
    return JsonResponse({"data":l})

def searchByDate(request):
    file_date = request.GET.get('file_date')
    if not file_date:
        return JsonResponse({'status': 'no folder given'})
    ex = Files.objects.values('file_name', 'folder_name', 'file_date', 'file_time', 'file_status', 'check',
                              'size').filter(file_date__iexact=file_date)
    l = []
    for f in ex:
        d = {}
        d['name'] = f['file_name']
        d['folder'] = f['folder_name']
        d['date'] = f['file_date']
        d['time'] = f['file_time']
        d['status'] = f['file_status']
        d['check'] = f['check']
        d['size'] = f['size']
        l.append(d)
    return JsonResponse({"data": l})

def twoDates(request):
    file_date1 = request.GET.get('file_date1')
    file_date2 = request.GET.get('file_date2')

    if not file_date1:
        return JsonResponse({'status': 'no folder given'})
    ex = Files.objects.values('file_name', 'folder_name', 'file_date', 'file_time', 'file_status', 'check',
                              'size').filter(file_date__range=[file_date1,file_date2])
    l = []
    for f in ex:
        d = {}
        d['name'] = f['file_name']
        d['folder'] = f['folder_name']
        d['date'] = f['file_date']
        d['time'] = f['file_time']
        d['status'] = f['file_status']
        d['check'] = f['check']
        d['size'] = f['size']
        l.append(d)
    return JsonResponse({"data": l})


def timeInterval(request):

    file_time = request.GET.get('file_time')
    value = request.GET.get('status')
    if not file_time:
        return JsonResponse({'status': 'no folder given'})
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    txt = current_time
    today = date.today()
    x=""
    if value=="sec":
        a = txt[6]
        b = txt[7]
        c = a + "" + b
        d = int(c) - int(file_time)
        x = txt.replace(str(c), str(d))
    if value=="min":
        a = txt[3]
        b = txt[4]
        c = a + "" + b
        if c < file_time:
            ac=int(file_time)-int(c)
            sixt=60-ac
            x=txt.replace(str(c),str(sixt))
            t1=txt[0]+""+txt[1]
            t2=int(t1)-1
            x=txt.replace(t1,str(t2))
        else:
            d = int(c) - int(file_time)
            x = txt.replace(str(c), str(d))
    if value=="hour":
        a = txt[0]
        b = txt[1]
        c = a + "" + b
        d = int(c) - int(file_time)
        x = txt.replace(str(c), str(d))

    ex = Files.objects.values('file_name', 'folder_name', 'file_date', 'file_time', 'file_status', 'check',
                              'size').filter(file_time__range=[x,current_time],file_date=today)
    l = []
    for f in ex:
        d = {}
        d['name'] = f['file_name']
        d['folder'] = f['folder_name']
        d['date'] = f['file_date']
        d['time'] = f['file_time']
        d['status'] = f['file_status']
        d['check'] = f['check']
        d['size'] = f['size']
        l.append(d)
    return JsonResponse({"data": l})


def bytimeDate(request):
    file_time = request.GET.get('file_time')
    file_date = request.GET.get('file_date')
    if not file_time:
        return JsonResponse({'status': 'no folder given'})
    a = file_time[3]
    b = file_time[4]
    ab=a+""+b
    c = a + "" + b+":00"
    d=a+""+b+":59"
    x = file_time.replace(ab, c)
    x1=file_time.replace(ab,d)

    ex=Files.objects.values('file_name','folder_name','file_date','file_time','file_status','check','size').filter(file_time__range=[x,x1],file_date=file_date)
    l = []
    for f in ex:
        d = {}
        d['name'] = f['file_name']
        d['folder']=f['folder_name']
        d['date'] = f['file_date']
        d['time'] = f['file_time']
        d['status'] = f['file_status']
        d['check'] = f['check']
        d['size'] = f['size']
        l.append(d)
    return JsonResponse({"data":l})

@csrf_exempt
def login(request):
    if request.method=='POST':
        username=request.POST.get('use')
        password=request.POST.get('pass')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            folder = Folder.objects.all()
            fol = Folder.objects.values('name')
            countFolder = len(folder)
            file = Files.objects.all()
            l = []
            for f in fol:
                l.append(f['name'])
            jsn = json.dumps(l);

            dic = {'fol_no': countFolder, 'file_no': len(file), 'fol_name': jsn}

            return render(request,'ftpmonitor/index.html',dic)
        else:
            messages.info(request,'invalid credentials')
    else:
        return render(request,'ftpmonitor/login.html')
    return render(request, 'ftpmonitor/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'ftpmonitor/login.html')
# @csrf_exempt
def register(request):
    if request.method == 'POST':

        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        username=request.POST.get('username')
        password1=request.POST.get('password')
        password2=request.POST.get('repassword')
        email=request.POST.get('email')
        print(first_name)
        user=User.objects.create_user(username=username , password=password1,email=email, first_name=first_name,last_name=last_name, is_staff=True)
        user.is_staff=True
        user.save();
        dic={'message':'Successfully Registered'}
        return render(request, 'ftpmonitor/register.html',dic)

    return render(request,'ftpmonitor/register.html')



