from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team


# Create your views here.
def new(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()



    return render(request,"home.html",{'result':obj,'result1':obj1})




#

 # return render(request,"result.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})


#
