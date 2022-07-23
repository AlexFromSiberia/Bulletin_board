from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Category')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT,
                                 verbose_name='Category')

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title



