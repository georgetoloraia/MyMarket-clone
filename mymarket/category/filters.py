import django_filters

from .models import Category, Info

class CategoryFilter(django_filters.FilterSet):
    nadzvisxe = django_filters.CharFilter(lookup_expr='exact')
    texnika = django_filters.CharFilter(lookup_expr='exact')
    iaragi = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Category
        fields = ['nadzvisxe', 'texnika', 'iaragi']

class InfoFilter(django_filters.FilterSet):
    telnumber = django_filters.CharFilter(lookup_expr='exact')
    images = django_filters.CharFilter(lookup_expr='icontains')
    mdebareoba = django_filters.CharFilter(lookup_expr='exact')
    text = django_filters.CharFilter(lookup_expr='icontains')
    salary = django_filters.NumberFilter(lookup_expr='gte')

    class Meta:
        model = Info
        fields = ['telnumber', 'images', 'mdebareoba', 'text', 'salary']
