from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    all_phones = Phone.objects.all()
    sort_type = request.GET.get('sort')
    if sort_type is not None:
        if sort_type == 'name':
            all_phones = Phone.objects.order_by(sort_type)
        if sort_type == 'max_price':
            all_phones = Phone.objects.order_by('-price')
        if sort_type == 'min_price':
            all_phones = Phone.objects.order_by('price')

    context = {'phones': all_phones, }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
