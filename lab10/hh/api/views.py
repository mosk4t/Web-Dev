from django.shortcuts import render

from django.shortcuts import get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Company, Vacancy
from .serializers import CompanySerializerManual, VacancySerializer



@api_view(['GET', 'POST'])
def company_list_fbv(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializerManual(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializerManual(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def company_detail_fbv(request, company_id): 
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'GET':
        serializer = CompanySerializerManual(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializerManual(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VacancyDetailAPIView(APIView):
    def get_object(self, vacancy_id):
        return get_object_or_404(Vacancy, pk=vacancy_id)

    def get(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyVacanciesAPIView(APIView):
    def get(self, request, company_id): 
        company = get_object_or_404(Company, pk=company_id)
        vacancies = company.vacancies.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


class TopTenVacanciesAPIView(APIView):
    def get(self, request):
        top_ten_vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(top_ten_vacancies, many=True)
        return Response(serializer.data)