from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

@csrf_exempt
def product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_list = list(products.values())
        return JsonResponse(products_list, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product(name=data['name'], price=data['price'])
        product.save()
        return JsonResponse({'id': product.id, 'name': product.name, 'price': product.price})
