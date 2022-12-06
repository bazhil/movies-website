from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Rating, RatingStar, Reviews, Actor

@admin.register(Category)
class CategoryAdmnin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name', )


class ReviewsInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [ReviewsInline]
    save_on_top = True
    save_as = True


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')

# admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre)
# admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
# admin.site.register(Reviews)
admin.site.register(Actor)
