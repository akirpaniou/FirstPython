from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponseNotFound
from django.template.response import TemplateResponse
from .forms import UserForm
from .forms import LesOne
from .forms import LesTwo
from .forms import LesTh
from .forms import LesF
from .models import Person



def index (request):
    header = "Personal Data"
    langs = ["English", "German", "Spanish"]
    user = {"name": "Tom", "age": 23}
    addr = ("Main Street", 23, 45)

    userform = UserForm()

    lang = ["English", "German", "French", "Spanish", "Chinese"]

    people = Person.objects.all()

    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "firstapp/index.html", {"people": people})

def indextwo(request):
    data = {"n": 0}
    return render(request, "firstapp/indextwo.html", context=data)
def abouttwo(request):
    lang = ["English", "German", "French", "Spanish", "Chinese"]
    return render(request, "firstapp/abouttwo.html", context={"langs": lang})
def about (request):
    return HttpResponse("About")
def contact (request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")


'''def crud(request):
    people = Person.objects.all()
    return render(request, "firstapp/crud.html", {"people": people})'''

def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/")

def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "firstapp/edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def lessforms(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        else:
            return HttpResponse("Invalid data")
    else:
        Les1 = LesOne()
        Les2 = LesTwo()
        Les3 = LesTh()
        Les4 = LesF()
        userform = UserForm()
        return render(request, "firstapp/forms.html", {"form": userform, "form1": Les1, "form2": Les2, "form3": Les3, "form4": Les4})

def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Product number {0} Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)

'''def users(request, id = 1, name = "Bob"):
    output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
    return HttpResponse(output)'''
def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
    return HttpResponse(output)

# Create your views here.
