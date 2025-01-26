from django.shortcuts import render,redirect
from home.models import *
from product.models import *


# Create your views here.
def index(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    slider = Slider.objects.all().order_by('-id')[0:6]
    about = About_Page.objects.all().order_by('-id')[0:1]
    contentclider = Content_Slider.objects.all().order_by('-id')
    service = Service.objects.all().order_by('-id')

    faq = FAQ.objects.all().order_by('-id')[0:6]


    
    

    page="home"
    context={
        'setting':setting,
        'slider':slider,
        'about':about,
        'contentclider':contentclider,
        'faq':faq,
        'service':service,
    }

    return render(request,'main/index.html',context)

def aboutus(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    about = About_Page.objects.all().order_by('-id')[0:1]
    slider = Slider.objects.all().order_by('-id')[0:6]
    
    

    page="home"
    context={
        'setting':setting,
        'slider':slider,
        'about':about,
    }

    return render(request,'main/about.html',context)



def product(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    product = Product.objects.all().order_by('?')

    page="home"
    context={
        'setting':setting,
        'product':product,
    }
    return render(request,'main/product/product.html',context)

def product_details(request,slug): 
    setting = Setting.objects.all().order_by('-id')[0:1]

    product = Product.objects.filter(slug = slug)
    if product.exists():
        product = Product.objects.get(slug = slug)
    else :
        return redirect('404')
    context = {

        'product': product,
        'setting': setting,
    }   
     
    return render(request, 'main/product/product-details.html',context)

#-------------------------Projects---------------------------------------------------------
def Complate_project(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    project = Project.objects.filter(Project_Type= 'COMPLATE').order_by('-id')


    page="home"
    context={
        'setting':setting,
        'project':project,
    }
    return render(request,'main/project/complate-projects.html',context)

def Ongoing_project(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    project = Project.objects.filter(Project_Type= 'ONGOING').order_by('-id')


    page="home"
    context={
        'setting':setting,
        'project':project,
    }
    return render(request,'main/project/Ongoing-Projects.html',context)

def Upcoming_project(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    project = Project.objects.filter(Project_Type = 'UPCOMING').order_by('-id')

    page="home"
    context={
        'setting':setting,
        'product':product,
    }
    return render(request,'main/project/Upcoming-Projects.html',context)

def project_details(request,slug): 
    setting = Setting.objects.all().order_by('-id')[0:1]

    project = Project.objects.filter(slug = slug)
    if project.exists():
        project = Project.objects.get(slug = slug)
    else :
        return redirect('404')
    context = {

        'project': project,
        'setting': setting,
    }   
     
    return render(request, 'main/project/product-details.html',context)

#-------------------------Projects---------------------------------------------------------


def service(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    service = Service.objects.all().order_by('?')

    page="home"
    context={
        'setting':setting,
        'service':service,
    }
    return render(request,'main/services/services.html',context)

def service_details(request,slug): 
    setting = Setting.objects.all().order_by('-id')[0:1]

    service = Service.objects.filter(slug = slug)
    if service.exists():
        service = Service.objects.get(slug = slug)
    else :
        return redirect('404')
    context = {

        'service': service,
        'setting': setting,
    }   
     
    return render(request, 'main/services/services-details.html',context)



def faqs(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/FQA.html',context)

def contactus(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/contactus.html',context)

def BRAND(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/BRAND.html',context)

def BLOG(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/blog.html',context)

def Gallery_Media(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    gallery = Gallery.objects.all().order_by('?')


    page="home"
    context={
        'setting':setting,
        'gallery':gallery,
    }
    return render(request,'main/Gallery.html',context)


def Our_Team(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/OurtTeam.html',context)


def Vision_Mission(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Vision-Mission.html',context)

def DirectorDesk(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/director-desk.html',context)


#=====================Service Area=================================
def Architecture(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Architecture.html',context)


def Construction(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Construction.html',context)


def Interior(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Interior.html',context)



def Landscape(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Landscape.html',context)


def Turnkey(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Turnkey.html',context)


def REALESTATE(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Real_Estate.html',context)