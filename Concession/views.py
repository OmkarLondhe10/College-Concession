from django.http import HttpResponse , JsonResponse
from django.shortcuts import render, redirect
from service.models import services 
from input.models import output 
from django.shortcuts import get_object_or_404, render

def homePage(request):
    return render(request, "main.html")

def about(request):
    return render(request, "about.html")

def concession(request):
    return render(request, "concession.html")

def contact(request):
    return render(request, "contact.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def mainPage(request):
    return render(request, "main.html")

def panel(request):
    return render (request, "panel.html")

def saveEnquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        services.objects.create(name=name, email=email, subject=subject, message=message)

        return render(request, "contact.html", {"success": "Enquiry submitted successfully!"})

    return render(request, "contact.html", {"error": "Invalid request method."})


def input(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        year = request.POST.get('year')
        branch = request.POST.get('branch')
        start = request.POST.get('start')  
        end = request.POST.get('end')  

        en = output(
            name=name,
            email=email,
            year=int(year),
            branch=branch,
            start_destination=start,
            end_destination=end
        )
        en.save()
        return redirect('panel')  

    return render(request, "concession.html")




def panel_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            id_to_delete = request.POST.get('id')
            if id_to_delete:
                output.objects.filter(id=id_to_delete).delete()

    query = request.POST.get('query')
    if query:
        form = output.objects.filter(name__icontains=query) | output.objects.filter(email__icontains=query)
    else:
        form = output.objects.all().order_by('-submit_time')

