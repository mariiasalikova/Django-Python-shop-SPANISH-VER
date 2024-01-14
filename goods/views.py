from django.shortcuts import render

# Create your views here.


def catalog(request):
    context = {
        "title": "Home catalog",
        "goods": [
            {
                "image": "",
                "name": "",
                "description": "",
                "price": 150.00,
            }
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
