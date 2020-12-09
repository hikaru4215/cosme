from django.contrib import admin
from .models import Recommenditem, Category, Price, Score

admin.site.register(Recommenditem)
admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Score)