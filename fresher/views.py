from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Fresher
from .serializers import FresherSerializer

# Create your views here.

def freshersHome(request):
    allPosts = Fresher.objects.all()
    # serializer = FresherSerializer(allPosts, many=True)
    # return JsonResponse(serializer.data, safe=False)
    context = {'allPosts':allPosts}
    return render(request, 'fresher/fresherHome.html', context)


def fresherPost(request, slug):
    post = Fresher.objects.filter(slug=slug).first()
    # if posts is not None:
    #     serializer = FresherSerializer(posts)
    #     return JsonResponse(serializer.data, safe=False)
    # else:
    #     return JsonResponse({"message":"Post Not Found"})    
    context = {'post': [post]}
    return render(request, 'fresher/fresherPage.html', context) 



def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Fresher.objects.none()
    else:
        allPostsTitle = Fresher.objects.filter(profile__icontains=query)
        allPostsContent = Fresher.objects.filter(company__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)    
    context = {'allPosts':allPosts, 'query':query}
    return render(request, 'home/search.html', context)