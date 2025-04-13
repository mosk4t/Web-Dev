from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255) 

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories" 

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Product(models.Model):
    name = models.CharField(max_length=255)        
    price = models.FloatField()                     
    description = models.TextField()               
    count = models.IntegerField()                   
    is_active = models.BooleanField(default=True)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
            'category_id': self.category_id 
        }