from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Comment
import calendar
from datetime import datetime, timedelta


# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {"courses":courses})

def submit(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST["name"], description=request.POST["description"])
        print Course.objects.all()
        return redirect('/')
    elif request.method == 'GET':
        return redirect('/')

def delete(request, id):
    # query for deleteion
    try:
        target = Course.objects.get(id=id)
        target.localtime = utc_to_local(target.created_at)
    except Course.DoesNotExist:
        messages.add_message(request, messages.INFO, "Course not found!")
        return redirect('/')
    return render(request, 'course/delete.html', {"target":target})

def destroy(request, id):
    if request.method == 'POST':
        Course.objects.filter(id=id).delete()
    return redirect('/')

def comments(request, id):
    try:
        target = Course.objects.get(id=id)
    except Course.DoesNotExist:
        messages.add_message(request, messages.INFO, "Course not found!")
        return redirect('/')
    try:
        comments = Comment.objects.filter(course=id)
    except Comment.DoesNotExist:
        comments = []
    return render(request, 'course/comments.html', {"target":target, "comments":comments})

def addComment(request, id):
    if request.method == 'POST':
        newcomment = Comment.objects.addComment(request.POST, id)
        if newcomment[0] == False:
            for msg in newcomment[1]:
                messages.add_message(request, messages.INFO, msg)
        return redirect('/comments/{}'.format(id))
    else:
        return redirect('/comments/{}'.format(id))

def deleteComment(request, id):
    redir_id = Comment.objects.get(id=id).course.id
    if request.method == 'POST':
        error_code = Comment.objects.removeComment(request.POST, id)[1]
        for msg in error_code:
            messages.add_message(request, messages.INFO, msg)
        return redirect('/comments/{}'.format(redir_id))
    else:
        return redirect('/comments/{}'.format(redir_id))
