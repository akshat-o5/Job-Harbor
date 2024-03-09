from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Internship
from .serializers import InternshipSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def internshipHome(request):
    allPosts = Internship.objects.all()
    # serializer = InternshipSerializer(allPosts, many=True)
    # return JsonResponse(serializer.data, safe=False)
    context = {'allPosts':allPosts}
    return render(request, 'internship/internshipHome.html', context)



def internshipPost(request, slug):
    post = Internship.objects.filter(slug=slug).first()
    # if post is not None:
    #     if request.method == 'GET':
    #         serializer = InternshipSerializer(post)
    #         return JsonResponse(serializer.data, safe=False)
    #     elif request.method == 'DELETE':
    #         post.delete()
    #         return JsonResponse({"message": "Post deleted successfully"})
    # else:
    #     return JsonResponse({"message": "Post Not Found"})
    context = {'post': [post]}
    return render(request, 'internship/internshipPage.html', context) 



def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Internship.objects.none()
    else:
        allPostsTitle = Internship.objects.filter(profile__icontains=query)
        allPostsContent = Internship.objects.filter(company__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)    
    context = {'allPosts':allPosts, 'query':query}
    return render(request, 'home/search.html', context)