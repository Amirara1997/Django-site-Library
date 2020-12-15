from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Buyer
from django.utils import timezone


def home2(request):
    return render(request, 'buyer/home2.html')
    # ,'hunter/home.html',{'buyers':buyers})
def home3(request):
    return render(request, 'buyer/home3.html')

def home4(request):
    return render(request, 'buyer/home4.html')


@login_required
def creater(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] :
                # and request.POST['body2']:
                # and request.POST['url']
            # and request.FILES['icon'] and request.FILES['image']:
            #  جای این کامنت در خط بالا ما بین بادی و آیکون برای زمانی که کتاب ها به لینکی نیاز داشته باشند و قسمتی هم در جزئیات کامنت شده است
            buyer = Buyer()
            buyer.title = request.POST['title']
            buyer.body = request.POST['body']
            # buyer.body2 = request.POST['body2']
            # if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
            #     buyer.url = request.POST['url']
            # else:
            #     buyer.url = 'http://' + request.POST['url']
            # hunter.icon = request.FILES['icon']
            # hunter.image = request.FILES['image']
            buyer.pub_date = timezone.datetime.now()
            buyer.buyer = request.user
            buyer.save()
            return redirect('home2')

        else:
            return render(request, 'buyer/creater.html',{'error':'تمام فیلد ها باید تکمیل شود.'})
    else:
        return render(request, 'buyer/creater.html')
