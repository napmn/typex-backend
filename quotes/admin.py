from django.contrib import admin

from quotes.models import Author, Quote

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('perex', 'author', 'quote_type')
