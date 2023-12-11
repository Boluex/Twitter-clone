from django.shortcuts import render,redirect,reverse
from django.db.models import Q
from django.contrib.auth.models import User
from.models import posts,comment,follow_button,like_button
from django.contrib import messages
from django.http import HttpResponse
from users.models import profile
from.forms import update_comment,update_posts
import random
# Create your views here.
def post_update(request,id):
    form=update_posts()
    if request.method == 'POST':
         get_post=posts.objects.get(id=id)
         if request.user== get_post.user:
              form=update_posts(request.POST,request.FILES,instance=get_post)
              if form.is_valid():
                  form.save()
                  return redirect(reverse(detail,args=[id]))
         messages.error(request,'action denied')
         return render(request,'twitter/comment_post.html',{'form':form})
    return render(request,'twitter/comment_post.html',{'form':form})

def post_delete(request,id):
         get_post=posts.objects.get(id=id)
         if request.user== get_post.user:
             get_post.delete()
             return redirect(reverse(detail,args=[id]))
         messages.error(request,'action denied')
         return redirect(reverse(detail,args=[id]))
def home(request):
    all_post=posts.objects.all().order_by('-id')
    user_all=[]

    all_users=User.objects.all()
    all_followers = follow_button.objects.all()
    all_following = follow_button.objects.filter(following=request.user)
    followers = follow_button.objects.filter(follower=request.user).count()
    following = follow_button.objects.filter(following=request.user).count()
    # random.shuffle(all_users)

    if like_button.objects.filter(user=request.user).exists():
        like_value='unlike'

    else:
        like_value = None
    # if follow_button.objects.filter(following=request.user,follower=follower).exists():
    #     follow_value='unfollow'
    # else:
    #     # follow_value = None

    return render(request,'twitter/home.html',{'all_followers':all_followers,'all_following':all_following,'posts':all_post,'followers':followers,'following':following,'like_value':like_value,'all_users':all_users[:4]})

def detail(request,id):
    get_post=posts.objects.get(id=id)
    filter_comments=comment.objects.filter(post=get_post)
    return render(request,'twitter/detail.html',{'post':get_post,'comments':filter_comments})

def delete(request,id):
    get_post=posts.objects.get(id=id)
    if request.user == get_post.author:
        get_post.delete()
        messages.success(request,'deleted successfully')
        return redirect('/')
    messages.error(request,'invalid action')
    return redirect('/')


def create(request):
    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        image=request.FILES.get('image')
        new_post=posts(title=title,content=content,image=image,author=request.user)
        new_post.save()
    return render(request,'twitter/new.html')


def create_comment(request,id):
    if request.method == 'POST':
        # user = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        post=posts.objects.get(id=id)
        new_comment=comment(user=request.user,content=content,image=image,post=post)
        new_comment.save()
        messages.success(request,'comment saved')
        return redirect(reverse(detail,args=[id]))
    return HttpResponse('Not a POST action')


def all_comments(request,id):
    get_post=posts.objects.get(id=id)
    filter_comments=comment.objects.filter(post=get_post)
    return render(request,'twitter/comments.html',{"posts":filter_comments})


def search(request):
    if request.method == 'GET':
        search_name=request.GET.get('search')
        if search_name:
            # result=Q(Q(title__icontains=search_name)|Q(content__icontains=search_name))
            result=Q(Q(username__icontains=search_name))
            get_result=User.objects.filter(result)
            return render(request,'twitter/search.html',{'post':get_result})
        return render(request, 'twitter/search.html', {})
    return HttpResponse('Not a post method')



def likee(request,id):
    get_post=posts.objects.get(id=id)
    user=request.user
    if like_button.objects.filter(user=user,post=get_post).exists():
        get_button=like_button.objects.get(user=user,post=get_post)
        get_button.delete()
        return redirect('/')
    new_button=like_button(post=get_post,user=user)
    new_button.save()
    return redirect('/')

def about(request):
    pass
def userposts(request,**kwargs):
    get_user=User.objects.get(username=kwargs.get('username'))
    filter_post_by_user=posts.objects.filter(author=get_user)
    return render(request,'twitter/userposts.html',{'posts':filter_post_by_user})

def update(request,id):
    pass

def followers_view(request):
    # get_user=User.objects.get(username=kwargs.get('username'))
    all_users = User.objects.all()
    filter_followers=follow_button.objects.filter(follower=request.user)
    followers = follow_button.objects.filter(follower=request.user).count()
    following = follow_button.objects.filter(following=request.user).count()

    return render(request,'twitter/followers.html',{'posts':filter_followers,'all_users':all_users,'following':following,'followers':followers})

def following_view(request):
    # get_user=User.objects.get(username=kwargs.get('username'))
    all_users = User.objects.all()
    filter_followers = follow_button.objects.filter(following=request.user)
    followers = follow_button.objects.filter(follower=request.user).count()
    following = follow_button.objects.filter(following=request.user).count()
    return render(request, 'twitter/following.html',
                  {'posts': filter_followers, 'all_users': all_users, 'following': following, 'followers': followers})


def create_followers(request,username):
    if request.method =='POST':
        get_user = User.objects.get(username=username)
        if follow_button.objects.filter(following=request.user,follower=get_user).exists():
            get_follow_button=follow_button.objects.get(following=request.user,follower=get_user)
            get_follow_button.delete()
            return redirect('/')
        new_button=follow_button(follower=get_user,following=request.user)
        new_button.save()
        return redirect('/')
    return HttpResponse('check your code')
def view_profile(request,username):
    if request.method == "POST":
        get_user=User.objects.get(username=username)
        get_user_profile=profile.objects.get(user=get_user)
        followers = follow_button.objects.filter(follower=get_user.id).count()
        following = follow_button.objects.filter(following=get_user.id).count()
        if follow_button.objects.filter(follower=request.user,following=get_user.id).exists():
            follow_value='unfollow'
        else:
            follow_value = None
        return render(request,'twitter/user_profile.html',{'profile':get_user_profile,'following':following,'followers':followers,'follow_value':follow_value})
    return HttpResponse('not a POST method')

