from django.core.urlresolvers import reverse

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from testtinymce.testapp.models import TestPage
from tinymce.widgets import TinyMCE
from comics.models import Comic, CustomFlatPage
from comics.seo import MyMetadata

from django.contrib.sites.models import Site


from rollyourown.seo.admin import register_seo_admin, get_inline
register_seo_admin(admin.site, MyMetadata)

class ComicAdmin(admin.ModelAdmin):
#    inlines = [ get_inline(MyMetadata) ]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Comic, ComicAdmin)

class TinyMCEFlatPageAdmin(FlatPageAdmin):
    inlines = [ get_inline(MyMetadata) ]
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "sites": 
            kwargs["initial"] = [Site.objects.get_current()]
        return super(TinyMCEFlatPageAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
            ))
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class TinyMCETestPageAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content1', 'content2'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
            ))
        return super(TinyMCETestPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.unregister(FlatPage)
admin.site.unregister(Site)
admin.site.register(CustomFlatPage, TinyMCEFlatPageAdmin)

