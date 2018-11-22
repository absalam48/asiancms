from django.contrib import admin
from blog.models import Author, Blog, Entry, About, Service, Contact
# Register your models here.

admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Contact)
