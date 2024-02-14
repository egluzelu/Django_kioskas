from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner',]
    list_display_links = ['name', 'owner']
    list_filter = ['owner']
    search_fields = ['name']
    fieldsets = (
        (_("general").title(), {
            "fields": (
                ('name'),
                'description',
            ),
        }),
        (_("ownership").title(), {
            "fields": (
                ('owner'),
            ),
        }),
    )
    

    def total_blog(self, obj: models.Blog):
        return obj.blog.count()
    total_blog.short_description = _("total blogs")

    def recent_blog(self, obj: models.Blog):
        return "; ".join(obj.blog.order_by('-created_at').values_list('name', flat=True)[:3])
    recent_blog.short_description = _("recent blogs")


admin.site.register(models.Blog, BlogAdmin)
