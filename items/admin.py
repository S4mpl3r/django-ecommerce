from django.contrib import admin

from .models import Category, Item, Purchase

admin.site.register([Category, Item, Purchase])
