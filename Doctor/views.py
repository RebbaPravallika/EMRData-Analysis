

from django.shortcuts import render
from . models import doc
# Create your views here.
def docregister(request):
    if(request.method == 'POST'):
        doc_id = int(request.POST['id_no'])
        fname = request.POST['nam']
        dept = request.POST['department']
        hos = request.POST['hospital']
        contact = request.POST['contact-no']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if(password == cpassword):
            user = doc(fname=fname,docid=doc_id,department=dept,hospital=hos,contact=contact,
                       email=email,password=password,cpassword=cpassword)
            user.save()
        v = doc.objects.all()
        for i in v:
            print(i.fname)
        #return redirect('/')
        return render(request,'test.html')
        
    else:    
        return render(request,'docregister.html')

def doclogin(request):
    if(request.method == 'POST'):
        v=doc.objects.all()
        logId = int(request.POST['logId'])
        logPw = request.POST['logPw']
        for i in v:
            if(i.docid==logId and i.password==logPw):
                return render(request,'test.html')
    
    else:
        return render(request,'doclogin.html')
    
def heart(request):
    return render(request,'heart.html')

def bcancer(request):
    return render(request,'bcancer.html')

def dia(request):
    return render(request,'dia.html')


