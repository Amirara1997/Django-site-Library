from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hunter
from django.utils import timezone
from buyer.models import Buyer

def home(request):
    hunters =Hunter.objects
    return render(request,'hunter/home.html',{'hunters':hunters})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body']  and request.FILES['icon'] and request.FILES['image']:
            # and request.POST['url']: جای این کامنت در خط بالا ما بین بادی و آیکون برای زمانی که کتاب ها به لینکی نیاز داشته باشند و قسمتی هم در جزئیات کامنت شده است
            hunter = Hunter()
            hunter.title = request.POST['title']
            hunter.body = request.POST['body']
            # if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
            #     hunter.url = request.POST['url']
            # else:
            #     hunter.url = 'http://' + request.POST['url']
            hunter.icon = request.FILES['icon']
            hunter.image = request.FILES['image']
            hunter.pub_date = timezone.datetime.now()
            hunter.hunter = request.user
            hunter.save()
            return redirect('home')

        else:
            return render(request, 'hunter/create.html',{'error':'تمام فیلد ها باید تکمیل شوند.'})
    else:
        return render(request, 'hunter/create.html')


def detail(request, hunter_id):
    hunter = get_object_or_404(Hunter, pk=hunter_id)
    return render(request, 'hunter/detail.html',{'hunter':hunter})

@login_required(login_url="/accounts/signup")
def upvote(request, hunter_id):
    if request.method == 'POST':
        hunter = get_object_or_404(Hunter, pk=hunter_id)
        hunter.votes_total += 1
        hunter.save()
        return redirect('/hunters/' + str(hunter_id))



def home2(request):
    buyers =Buyer.objects
    return render(request,'buyer/home2.html')