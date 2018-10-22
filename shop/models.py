from django.urls import reverse
from django.db import models

#Модель категорії
class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.CharField(max_length=200, db_index=True, unique=True)

	def get_absoluteurl(self):
		return reverse('shop:ProductListByCategory', args=[self.slug])

	class Meta:
		ordering = ['name']
		verbose_name = 'Категорія'
		verbose_name_plural = 'Категорії'

	def __str__(self):
		return self.name


#Модель продукту
class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', verbose_name="Категорія", on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True, verbose_name="Назва")
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Зображення товару")
	description = models.TextField(blank=True, verbose_name="Опис")
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
	stock = models.PositiveIntegerField(verbose_name="На складі")
	available = models.BooleanField(default=True, verbose_name="Доступно")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def get_absoluteurl(self):
		return reverse('shop:ProductListByCategory', args=[self.id, self.slug])

	class Meta:
		ordering = ['name']
		index_together = [['id', 'slug']]

	def __str__(self):
		return self.name