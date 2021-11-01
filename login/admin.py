from django.contrib import admin

# Register your models here.
from login.models import Contact, Product, Category, Enquire, Post

admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Enquire)
admin.site.register(Post)
