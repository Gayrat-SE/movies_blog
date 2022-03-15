from . import forms
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *



class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'

# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","url")
    list_display_links = ("name","id",)
    
    
class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 0
    readonly_fields = ("name", "email",) 
class MovieShotsInline(admin.TabularInline):
    model = Movieshots
    extra = 0
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} witdh=60px height=60px')
    
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year","category","url","draft",)
    list_display_links = ("title",)
    list_filter = ("category","year",)
    search_fields = ("title","category__name")
    inlines = [MovieShotsInline,ReviewInline]
    form = MovieAdminForm
    save_on_top = True
    list_editable = ["draft"]
    # fields = (("actors", "directors", "genres"),)
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields":(("title","tagline"),)
        }),
        (None, {
            "fields":("description",)
        }),
        ("About", {
            "fields":(("genres","category","get_image",),)
        }),
        (None, {
            "fields":(("year","country","world_premier"),)
        }), 
        ("actors", {
            "classes":("collapse",),
            "fields":(("directors","actors",),)
        }),
        ("budget", {
            "classes":("collapse",),
            "fields":(("budget","fees_in_usa","fees_over_world"),)
        }),
        ("options", {
            "fields":(("url","draft"),)
        })
        
    )

    

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} witdh=100px height=100px')
    
    
@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email","parent","movie","id")
    readonly_fields = ("name", "email")

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} witdh=100px height=100px')
    
    get_image.short_description = "Director Images"    


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
  
  
@admin.register(Movieshots)
class MovieshotAdmin(admin.ModelAdmin):
    list_display = ("title", "movie","get_image")  
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} witdh=100px height=100px')
    
    get_image.short_description = "movie shots"


@admin.register(RatingStars)
class ReytingStarsAdmin(admin.ModelAdmin):
    list_display = ("value",)
    
    
@admin.register(Reyting)
class ReytingAdmin(admin.ModelAdmin):
    list_display = ("ip",)


admin.site.site_title = "Movies-Admin"
admin.site.site_header = "Movies-Admin"