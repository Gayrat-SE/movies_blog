from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Movieshots)
admin.site.register(RatingStars)
admin.site.register(Reyting)
admin.site.register(Reviews)