from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from crud.forms import UserModelForm
from .models import UserModel
# Create your views here.
def index(request):
    return redirect(create)
    
def create(request):
    
    # if request.method == 'POST':
    #     firstname=request.POST['firstname']
    #     lastname=request.POST['lastname']
    #     photo=request.FILES['photo']
    #     user_data=UserModel.objects.create(
    #         firstname=firstname,
    #         lastname=lastname,
    #         )
    #     user_data.save()

    if request.method == 'POST':
        Userdata_upload = UserModelForm(request.POST, request.FILES)
        if Userdata_upload.is_valid():
            Userdata_upload.save()
            return redirect(index)
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "create">reload</a>""")
    else:
        p={
            'userForm':UserModelForm,
        }
        return render(request, 'create.html',p)
    
def read(request):
    user_data=UserModel.objects.all()

    p={
        'user_data':user_data,    
    }
    return render(request, 'read.html', p)

def update(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(UserModel, id = id)
 
 
    # pass the object as instance in form
    form = UserModelForm(request.POST or None, request.FILES or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect(read)
 
    # add form dictionary to context
    context["userForm"] = form
 
    return render(request, "update.html", context)
    
def delete(request, id):
    user_id=get_object_or_404(UserModel, id=id)
    user_id.delete()
    p={
        
    }
    return redirect(read)
    


