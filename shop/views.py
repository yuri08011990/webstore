from django.shortcuts import render, get_object_or_404
from .models import Category, Product

#Сторінка з товарами
def ProductList(request, categry_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if categry_slug:
		category = get_object_or_404(Category, slug=categry_slug)
		products = products.filter(category=category)
	return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products})

#Сторінка товару
def ProductDetail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	return render (request, 'shop/product/detail.html', {'product': product})