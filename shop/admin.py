from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe
from django_ckeditor_5.widgets import CKEditor5Widget

from django.contrib import admin

# Register your models here.
from .models import  Category, Product, ProducPhoto



from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget



# class CommentForm(forms.ModelForm):
#       """Form for comments to the article."""
#
#       def __init__(self, *args, **kwargs):
#           super().__init__(*args, **kwargs)
#           self.fields["description"].required = False
#
#       class Meta:
#           model = Product
#           fields = ("name", "description")
#           widgets = {
#               "description": CKEditor5Widget(
#                   attrs={"class": "django_ckeditor_5"}, config_name="comment"
#               )
#           }




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name','slug')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


class ProducPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')
    list_display_links = ('id', 'product')
    class Meta:
        model = ProducPhoto


class ProducPhotoInline(admin.TabularInline):
    model = ProducPhoto
    extra = 0
    readonly_fields = ('display_photo',)

    def display_photo(self, instance):
        if instance.photo:
            return mark_safe(f"<img src='{instance.photo.url}' width='50'>")
        return None

    display_photo.short_description = 'Photo'


admin.site.register(ProducPhoto, ProducPhotoAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'name','category', 'price','offer_id','vendor_code','picture1','size','color')
    list_display_links = ('category',)
    list_filter = ['name','category']
    list_editable = ['price',]
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProducPhotoInline] # Тут звязок з фотографіями


    # def get_photo(self, obj):
    #     if obj.producphoto_set.exists():
    #         photo_url = obj.producphoto_set.first().photo.url
    #         return mark_safe(f"<img src='{photo_url}' width='50'>")
    #     return None
    # def get_html_photo(self, object):
    #     return mark_safe(f"<img src='{object.photo.url}' width=50>")
    # get_photo.short_description = 'Photo'

    class Meta:
        model = Product



admin.site.register(Product, ProductAdmin)


