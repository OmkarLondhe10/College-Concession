from django.http import HttpResponse
from django.shortcuts import render , redirect
from contact.models import Contact
from concession.models import Concession

def homepage(request):
    return render(request,"main.html")

def aboutpage(request):
    return render(request,"about.html")

def concessionpage(request):
    return render(request,"concession.html")

def contactpage(request):
    return render(request,"contact.html")

def adminpage(request):
    if not request.session.get('is_admin_logged_in'):
        return redirect('login')
    data = Concession.objects.all()
    return render(request, 'admin.html', {'data': data})


def admin_view(request):
    return render(request, 'admin.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin@123':
            request.session['is_admin_logged_in'] = True
            return redirect('adminpage')  # 🔁 redirect by name
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()  # 🔁 Clears all session data
    return redirect('login')



def saveContact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        en=Contact(name=name,email=email,subject=subject,message=message)
        en.save()
    return render(request,"contact.html")

def saveConcession(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll=request.POST.get('roll')
        year=request.POST.get('year')
        branch=request.POST.get('branch')
        start_dest=request.POST.get('start')
        end_dest=request.POST.get('end')
        period=request.POST.get('period')

        rn=Concession(name=name,email=email,roll=roll,year=year,branch=branch,start_dest=start_dest,end_dest=end_dest,period=period)
        rn.save()
    return render(request,"concession.html")

def add_student(request):
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        roll=request.POST.get('roll')
        year=request.POST.get('year')
        branch=request.POST.get('branch')
        start_dest=request.POST.get('start')
        end_dest=request.POST.get('end')
        period=request.POST.get('period')

        rn=Concession(name=name,email=email,roll=roll,year=year,branch=branch,start_dest=start_dest,end_dest=end_dest,period=period)
        rn.save()

        return redirect("adminpage")
    return render(request,"admin.html")

def deleteConcession(request, id):
    student = Concession.objects.get(id=id)
    student.delete()
    return redirect('adminpage')

def printable_form(request, student_id):
    student = Concession.objects.get(id=student_id)
    return render(request, 'form.html', {'student': student})
