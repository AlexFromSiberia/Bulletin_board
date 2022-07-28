from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Bb, Category
from .forms import BbForm



def index(request):
    bbs = Bb.objects.all()
    categories = Category.objects.all()
    context = {'bbs': bbs, 'categories': categories}
    return render(request, 'bboard/index.html', context)


def by_category(request, category_id):
    bbs = Bb.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'bbs': bbs,
               'categories': categories,
               'current_category': current_category,
    }
    return render(request, 'bboard/by_category.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    success_url = reverse_lazy('create')
    form_class = BbForm



