import random

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=75,unique=True, verbose_name='نام دسته بندی')
    # slug = models.SlugField(blank=True, unique=True, allow_unicode=True, verbose_name='آدرس دسته بندی')

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(str(self.name) + "-" + str(random.randint(0, 400)))
    #     super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها '


class Book(models.Model):
    title = models.CharField(max_length=75, verbose_name='عنوان کتاب')
    author = models.CharField(max_length=75, verbose_name='نویسنده')
    # slug = models.SlugField(blank=True, allow_unicode=True, verbose_name='آدرس کتاب')
    inventory = models.PositiveIntegerField(verbose_name='تعداد')
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    unit_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت واحد')
    percent_discount = models.PositiveIntegerField(blank=True, null=True, verbose_name='تخفیف درصدی')
    cash_discount = models.PositiveIntegerField(blank=True, null=True, verbose_name='تخفیف نقدی')
    image = models.ImageField(upload_to='images')
    available = models.BooleanField(default=True, verbose_name='موجود')

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'

    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(str(self.title) + "-" + str(random.randint(0, 400)))
    #     super(Book, self).save(*args, **kwargs)

    @property
    def total_price(self):
        if not self.percent_discount and not self.cash_discount:
            return self.unit_price
        elif self.percent_discount:
            total = (self.percent_discount * self.unit_price) / 100
            return int(self.unit_price - total)
        elif self.cash_discount:
            total = self.unit_price - self.cash_discount
            return int(total)
        return self.total_price

    def __str__(self):
        return self.title
