from django.urls import path
from . import views
#from .views import ArticleDetailView

from datetime import datetime

urlpatterns = [
    path('', views.newsListView, name='news-home'),
    path('archive/', views.archiveListView, name='archive'),
    path('search/', views.SearchView, name='global-search'),
    path('search/<str:query>/<str:topic>/', views.SearchView_Filter, name='global-search-filter'),
    path('article/<int:pk>-<slug:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),

    path('sources/<str:source>/', views.source, name='source'),
    path('sports/<path:source>/<str:topic>/', views.sportsListView, name='category-sports')
    
    #path('letters/', views.lettersListView, name='category-letters'),
    #path('search/', views.SearchView.as_view(), name='global-search'),
    #path('others/', views.othersListView,    name='category-others'),
    #path('sports/', views.sportsListView, name='category-sports'),
    #path('<path:src>/sports/', views.sportsListView, name='category-sports'),
    #path('source/kaieteur/', views.source01_ListView, name='source-kaieteur'),
    #path('source/stabroek/', views.source02_ListView, name='source-stabroek'),
    #path('kaieteur/', views.source01_ListView, name='source-kaieteur'),
    #path('stabroek/', views.source02_ListView, name='source-stabroek')
    
]
