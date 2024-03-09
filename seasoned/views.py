from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Seasoned
from .serializers import SeasonedSerializer

# Create your views here.

def seasonedHome(request):
    allPosts = Seasoned.objects.all()
    # serializer = SeasonedSerializer(allPosts, many=True)
    # return JsonResponse(serializer.data, safe=False)
    context = {'allPosts':allPosts}
    return render(request, 'seasoned/seasonedHome.html', context)


def seasonedPost(request, slug):
    post = Seasoned.objects.filter(slug=slug).first()
    # if posts is not None:
    #     serializer = SeasonedSerializer(posts)
    #     return JsonResponse(serializer.data, safe=False)
    # else:
    #     return JsonResponse({"message":"Post Not Found"})    
    context = {'post': [post]}
    return render(request, 'seasoned/seasonedPage.html', context) 
    







def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Seasoned.objects.none()
    else:
        allPostsTitle = Seasoned.objects.filter(profile__icontains=query)
        allPostsContent = Seasoned.objects.filter(company__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)    
    context = {'allPosts':allPosts, 'query':query}
    return render(request, 'home/search.html', context)    