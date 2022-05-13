from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from cart.forms import CartAddProductForm
from .models import Product, Category


def category(request, slug):
    show = get_object_or_404(Category, slug=slug)
    product_category = show.products.all()
    paginator = Paginator(product_category, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    cart_product_form = CartAddProductForm()
    return render(request, 'category.html', {
        'product_category': product_category,
        'page_obj': page_obj, 'paginator': paginator,
        'cart_product_form': cart_product_form
    })


class Index(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'products'


def product_detail(request, slug, id):
    product = get_object_or_404(Product,
                                slug=slug,
                                id=id,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'view_product.html', {'product': product, 'cart_product_form': cart_product_form})
