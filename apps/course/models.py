from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommentManager(models.Manager):
    def addComment(self, postData, id):
        try:
            if len(postData["content"]) == 0:
                return (False, ["Comment cannot be empty!"])
        except KeyError:
            return (False, ["Key error - Comment cannot be empty!"])
        content = postData["content"]
        try:
            name = postData["name"]
            if len(name) == 0:
                name = "Anonymous"
                print "postData['name']", postData["name"]
        except KeyError:
            return (False, ["Invalid name"])
        try:
            password = postData["password"]
            if len(password) == 0:
                password = "password"
        except KeyError:
            password = "password"
        try:
            course = Course.objects.get(id=id)
        except (KeyError, Course.DoesNotExist):
            return (False, ["Invalid course ID"])

            # return (True, Comment.objects.create())
        return (True, Comment.objects.create(name=name, content=content, course=course, pw_hash=bcrypt.hashpw(password.encode(), bcrypt.gensalt())))
    def removeComment(self, postData, id):
        try:
            comment = Comment.objects.get(id=id)
        except Course.DoesNotExist:
            return (False, ["Invalid course ID"])
        try:
            password = postData["password"]
            if comment.pw_hash == bcrypt.hashpw(password.encode(), comment.pw_hash.encode()):
                comment.delete()
                return (True, ["Comment deleted!"])
            else:
                return (False, ["Incorrect deletion password!"])
        except KeyError:
            return (False, ["Invalid password"])


class Comment(models.Model):
    name = models.CharField(max_length=45)
    content = models.TextField(max_length=1000)
    pw_hash = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course)
    objects = CommentManager()
