from django.contrib import admin

from catalog.models import (CD, DVD, Book, Catalog, Contributor,
                            ContributorWithType, Magazine)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'catalog', 'isbn', 'dds', 'upc', )


admin.site.register(CD)
admin.site.register(DVD)
admin.site.register(Book, BookAdmin)
admin.site.register(Magazine)
admin.site.register(Catalog)
admin.site.register(Contributor)
admin.site.register(ContributorWithType)
