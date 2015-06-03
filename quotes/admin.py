from django.contrib import admin


from quotes.models import Author,Categories,Quote

admin.site.register(Author)
admin.site.register(Quote)
admin.site.register(Categories)


