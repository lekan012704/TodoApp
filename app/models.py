from django.db import models
from django.urls import reverse
# Create your models here.

class Todo(models.Model):
    status = (
        ('1', 'new'),
        ('2', 'in progress'),
        ('3', 'completed')
    )
    item = models.CharField(max_length=500)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    status= models.CharField(max_length=50, choices=status)

    class Meta:
        verbose_name =("Todo")
        verbose_name_plural =("Todos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Todo_detail", kwargs={"pk": self.pk})

