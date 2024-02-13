
from django.urls import path
from  . import views
app_name='pictureapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('picture/<int:picture_id>/',views.detail,name='detail'),
    path('add/',views.add_picture,name='add_picture'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete')
]