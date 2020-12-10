from django.contrib import admin
from .models import Recommenditem, Category, Price, Score, Review

admin.site.register(Recommenditem)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Score)