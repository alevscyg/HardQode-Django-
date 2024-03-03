from django.contrib import admin
from .models import Creators, Product, ProductMaxMinMembers, Users, UsersProducts, Lesson, Group

admin.site.register(Creators)
admin.site.register(Product)
admin.site.register(ProductMaxMinMembers)
admin.site.register(Users)
admin.site.register(UsersProducts)
admin.site.register(Lesson)
admin.site.register(Group)

