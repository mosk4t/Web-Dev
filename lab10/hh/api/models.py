from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    city = models.CharField(max_length=100)
    address = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name



class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return f"{self.name} ({self.company.name})"

