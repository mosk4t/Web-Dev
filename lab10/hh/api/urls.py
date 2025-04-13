from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list_fbv, name='company-list'),
    path('companies/<int:company_id>/', views.company_detail_fbv, name='company-detail'),
    path('vacancies/', views.VacancyListAPIView.as_view(), name='vacancy-list'),
    path('vacancies/<int:vacancy_id>/', views.VacancyDetailAPIView.as_view(), name='vacancy-detail'),
    path('companies/<int:company_id>/vacancies/', views.CompanyVacanciesAPIView.as_view(), name='company-vacancies'),
    path('vacancies/top_ten/', views.TopTenVacanciesAPIView.as_view(), name='vacancy-top-ten'),
]