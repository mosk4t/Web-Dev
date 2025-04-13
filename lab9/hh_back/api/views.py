from django.http import JsonResponse, Http404
from .models import Company, Vacancy

def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        data = [company.to_dict() for company in companies]
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)

def company_detail(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)

    if request.method == 'GET':
        data = company.to_dict()
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)

def company_vacancies(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)

    if request.method == 'GET':
        vacancies = company.vacancies.all()
        data = [vacancy.to_dict() for vacancy in vacancies]
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)

def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        data = [vacancy.to_dict() for vacancy in vacancies]
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)

def vacancy_detail(request, pk):
    try:
        vacancy = Vacancy.objects.get(pk=pk)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancy not found'}, status=404)

    if request.method == 'GET':
        data = vacancy.to_dict()
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)

def vacancy_top_ten(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(salary__isnull=False).order_by('-salary')[:10]
        data = [vacancy.to_dict() for vacancy in vacancies]
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)