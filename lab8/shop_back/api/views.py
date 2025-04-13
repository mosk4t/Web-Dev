from django.http import JsonResponse, Http404
from .models import Product, Category

def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = [product.to_dict() for product in products]
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    if request.method == 'GET':
        data = product.to_dict()
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)


def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = [category.to_dict() for category in categories]
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)


def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
         return JsonResponse({'error': 'Category not found'}, status=404)

    if request.method == 'GET':
        data = category.to_dict()
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)


def category_products(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
         return JsonResponse({'error': 'Category not found'}, status=404)

    if request.method == 'GET':
        products = Product.objects.filter(category=category)
        data = [product.to_dict() for product in products]
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)