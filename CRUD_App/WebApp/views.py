from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect 
from .forms import Userform
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def HomeView(request):
    if request.method=="POST":
        form=Userform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Added successfully.")
    form = Userform()
    users=User.objects.all()
    context={'form':form , 'users': users }
    return render(request,'home.html' , context)
    
def UpdateView(request , id ):
    user = User.objects.get(id=id)
    if request.method=="POST":
        form=Userform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,f"Updated successfully.")
            return redirect('Home')
        else:
            print(form.errors)
            for error in form.errors:
                messages.error(request,f"Error : {error}")
    form=Userform(instance=user)
    context={'form':form , 'id' : user.id}
    return render(request,'Update.html' , context)
  
def DeleteView(request , id ):
    user = User.objects.get(id=id).delete()
    messages.error(request,f"Deleted successfully.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', ''))
    
    