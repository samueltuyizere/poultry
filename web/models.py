from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=124)
    description = models.TextField()
    category = models.CharField(max_length=124)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products')
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title


class Order(models.Model):
    client = models.CharField(max_length=124)
    product = models.CharField(max_length=124)
    contact = models.CharField(max_length=124)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.client


class BlogPost(models.Model):
    title = models.CharField(max_length=124)
    description = models.TextField()
    image = models.ImageField(upload_to='blog')
    category = models.CharField(max_length=124)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    posted_by = models.CharField(max_length=124)
    description = models.TextField()
    content_id = models.CharField(max_length=24)
    content = models.CharField(max_length=124)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.posted_by
