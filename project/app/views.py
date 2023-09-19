from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Iitial_info,Family_info,Professional_info,Educational_info,Desired_person,Contact_info
# Create your views here.


def index(request):
    x=User.objects.all()
    context = {
    'x':x
     }
    return render(request,"index.html",context )


def initial_info(request):
    x=Iitial_info.objects.all()
    context = {
      'x':x
      }
    return render(request,"initial_info.html",context)

def family_info(request):
    x=Family_info.objects.all()
    context = {
    'x':x
     }
    return render(request,"family_info.html",context)


def professional_info(request):
    x=Professional_info.objects.all()
    context = {
    'x':x
     }
    return render(request,"professional_info.html",context)

def educational_info(request):
    x=Educational_info.objects.all()
    context = {
    'x':x
     }
    return render(request,"educational_info.html",context)

def desired_person(request):
    x=Desired_person.objects.all()
    context = {
    'x':x
     }
    return render(request,"desired_info.html",context)





def user_profile_with_all_info(request):
    username=request.session.get('username')
    password=request.session.get('password')
        
    user=User.objects.get(name=username,password=password)
    id=user.id
    if id:
        user=User.objects.get(id=id)
        name=user.name
        initial_info=Iitial_info.objects.get(user=user)
        family_info=Family_info.objects.get(user=user)
        educational_info=Educational_info.objects.get(user=user)
        professional_info=Professional_info.objects.get(user=user)
        desired_person=Desired_person.objects.get(user=user)

        context = {
            'id':id,
            'user':user,
            'name':name,
            'initial_info':initial_info,
            'family_info':family_info,
            'educational_info':educational_info,
            'professional_info':professional_info,
            'desired_person':desired_person

   
        }
        
        print(name, initial_info.full_name,family_info.total_members)
        return render(request,"user_profile.html",context)
    else:
        return render(request,"user_login.html")
    
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        print(username)
        print(password)

        request.session['username']=username
        request.session['password']=password
        print(request.session.get('username'))
        print(request.session.get('password'))
        
        user=User.objects.get(name=username,password=password)

        if user:
            return redirect('user_profile')       

    return render(request,"user_login.html")

def public_page(request):
    x=Iitial_info.objects.all()
    context = {
      'items':x,
      }
    print(request.session.get('password'))

    return render(request,"public_page.html",context)


def user_admin(request):
    return render(request,"admin_dashboard.html")

def logout(request):
      print(request.session.get('username'))
      print(request.session.get('password'))
      del request.session['username']
      return redirect('user_login')


def see_details(request,id):
    print(id)
    if id:
        user=User.objects.get(id=id)
        initial_info=Iitial_info.objects.get(user=user)
        family_info=Family_info.objects.get(user=user)
        educational_info=Educational_info.objects.get(user=user)
        professional_info=Professional_info.objects.get(user=user)
        desired_person=Desired_person.objects.get(user=user)

        context = {
            'id':id,
            'user':user,
            'initial_info':initial_info,
            'family_info':family_info,
            'educational_info':educational_info,
            'professional_info':professional_info,
            'desired_person':desired_person

   
        }
    return render(request,"see_details.html",context)


    
def show_contact_info(request,id):

    if id:
        user=User.objects.get(id=id)
        cotact_info=Contact_info.objects.get(user=user)
    

        context = {
            'id':id,
            'user':user,
            'contact':cotact_info,
   
        }

    return render(request,"show_contact_infor.html",context)    



    



