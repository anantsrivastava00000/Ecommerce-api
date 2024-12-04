from django.urls import path
from . import views

urlpatterns = [
    
    path('SINGER/', views.SINGER.as_view()),
    path('SINGER/<int:pk>', views.SINGER.as_view()),
    # path('singer/', views.singer), #---> function based
    # path('singer/<int:pk>', views.singer),
    path('SONG/', views.SONG.as_view()),
    path('SONG/<int:pk>', views.SONG.as_view()),

    # path('Singer/', views.Singer.asview())
]