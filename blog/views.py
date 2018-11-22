from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from blog.models import Entry, Blog, About, Author, Service
from blog.forms import ContactForm
# Create your views here.

#class IndexView(generic.ListView):

def index(request):
    #model = Entry
    entrys = Entry.objects.all()
    abouts = About.objects.all()
    services = Service.objects.all()
    template_name = 'blog/index.html'
    return render(request, template_name, {'entrys': entrys, 'abouts': abouts, 'services': services})


class AboutView(generic.ListView):
    model = About
    template_name = 'blog/about.html'
    context_object_name = 'about_us'

class ServiceView(generic.ListView):
    model = Service
    template_name = 'blog/service.html'
    context_object_name = 'services'

class DetailView(generic.DetailView):
    model = Entry
    template_name = 'blog/detail.html'
    context_object_name = 'blog_detail'

def contact(request):

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return success(request)


        else:
            print("The Form Is Invalid")

    return render(request, 'blog/contact.html', {'form': form})

def success(request):
    return render(request, 'blog/success.html')
