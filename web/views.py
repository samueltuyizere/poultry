from django.shortcuts import render
from .models import *


def home(request):
    home_products = Product.objects.all()
    home_posts = BlogPost.objects.all()
    return render(request, "index.html", {'home_products':home_products, 'home_posts':home_posts})


def products(request):
    all_products = Product.objects.all()
    return render(request, "products.html", {'all_products': all_products})


def product(request, id):
    if request.method == 'POST':
        product = request.POST['product']
        client = request.POST['client']
        amount = request.POST['amount']
        price = request.POST['price']

        insert = Order(product=product, client=client, amount=amount, price=price)

        insert.save()

        single_product = Product.objects.get(id=id)
        return render(request, "product.html", {'single_product': single_product, 'success': 'Your Order has been submitted successfully' })
    else:

        single_product = Product.objects.get(id=id)
    return render(request, "product.html", {'single_product': single_product})


def posts(request):
    all_posts = BlogPost.objects.all()
    return render(request, "posts.html", {'all_posts': all_posts})


def post(request, id):
    if request.method == 'POST':
        posted_by = request.POST['posted_by']
        description = request.POST['description']
        content = request.POST['content']

        insert = Comment(posted_by=posted_by, description=description, content=content)

        insert.save()

        single_post = BlogPost.objects.get(id=id)
        comments = Comment.objects.all().filter()
        return render(request, "post.html", {'single_post': single_post, 'comments': comments, 'success': 'Your comment has been submitted successfully'})

    else:

        single_post = BlogPost.objects.get(id=id)
        comments = Comment.objects.all().filter()
    return render(request, "post.html", {'single_post': single_post, 'comments': comments})
