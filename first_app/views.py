from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord 
# Create your views here.

def index(requests):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}

    my_dir = {'insert_me':"Hello I am from the view dot py  which is under first app in the template 11111111"}
    return render(requests,'first_app/index.html',context=date_dict)

