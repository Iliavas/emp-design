from django.db import models


class Element(models.Model):
    img = models.ImageField(upload_to="static/Element")
    descr = models.TextField()

    def __str__(self):
        return self.descr


class Resources(models.Model):
    name = models.TextField()
    image = models.ImageField(blank=True, upload_to="static/Res")

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    descirption = models.TextField()
    image = models.ImageField(blank=True, upload_to="static/PostImg")
    stack = models.ManyToManyField(Element, blank=True)
    resources = models.ManyToManyField(Resources)
    video = models.URLField(blank=True)
    type = models.ForeignKey(Type, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title