from django.contrib import admin

from catalog.models import (CD, DVD, Book, Catalog, Contributor,
                            ContributorWithType, Magazine)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'catalog', 'isbn', 'dds', 'upc', )


class CDAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'catalog', 'upc',)


class DVDAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'catalog', 'upc',)


class MagazineAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'catalog', 'upc', 'volume', 'issue',)


admin.site.register(CD, CDAdmin)
admin.site.register(DVD, DVDAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Catalog)
admin.site.register(Contributor)
admin.site.register(ContributorWithType)
