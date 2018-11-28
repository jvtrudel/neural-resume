from django.shortcuts import render, redirect
from django.views.generic import ListView

from user.models import User
#from user.forms import UserForm
from core.forms import AddressForm, PersonForm


def list(request):
    users=User.objects.all()
    return render(request, "users/list.html", {'object_list':users})

def update(request,id):
    user=User.objects.get(pk=id)
    #form=UserForm(instance=user)
    if request.method=='POST':
        personForm=PersonForm(request.POST)
        addressForm=AddressForm(request.POST)
    #if all([personform.is_valid(),addressForm.is_valid()]):
        #personForm.save()
        #addressForm.save()
        #user.addresses.add(addressForm)
    context={'personForm':personForm, "addressForm": addressForm,'id':id}
    return render(request,"users/update.html",context)
    #return render(request,"users/list.html")
    #if request.method=='POST':
    #    userForm=UserForm(request.POST)
#        if userform.is_valid():

def create(request):
    #form=UserForm(request.POST or None) 
    personForm=PersonForm(request.POST or None)
    addressForm=AddressForm(request.POST or None)
    print("request method: {}".format(str(request.method)))
    #if form.is_valid():
    #    if request.method=='POST':
    #        form.save()
    #        return redirect('users:list')

    context={'personForm':personForm, "addressForm": addressForm,'id':id}
    return render(request,"users/create.html", context)

def delete(request,id):
    user=User.objects.get(pk=id)
    user.delete()
    return redirect("users:list")


class UserListView(ListView):
    template_name='users/list.html'
    queryset=User.objects.all()
