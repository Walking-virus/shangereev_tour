from django.contrib import admin
from . models import Travel, Trips, Comment, Command, Timetable, Images, AboutUs, ContactUs
# admin.site.register(Travel)
# admin.site.register(Trips)
# admin.site.register(Comment)
admin.site.register(Command)
admin.site.register(Timetable)
admin.site.register(AboutUs)
admin.site.register(ContactUs)
# admin.site.register(Images)


class TravelInline(admin.TabularInline):
    model = Travel
    extra = 0


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Trips)
class TripsAdmin(admin.ModelAdmin):
    inlines = [TravelInline]


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, CommentInline]