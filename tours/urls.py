from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.about_us),
    path('header/', views.header, name='header'),
    path('timetable/', views.timetable, name='timetable'),
    path('command/', views.command, name='command'),
    path('about_us/', views.about_us, name='about_us'),
    path('trips/<slug:slug>/', views.page_travels, name='page_travels'),
    path('travel/<str:slug>/', views.detail_about_travel, name='detail_about_travel'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)