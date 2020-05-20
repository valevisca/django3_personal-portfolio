from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    # Using '<int:blog_id>' in the path tells urs.py to look for a integer
    # number in the url. Many other options are available, like '<str: >'
    path('<int:blog_id>/', views.detail, name='detail'),

]