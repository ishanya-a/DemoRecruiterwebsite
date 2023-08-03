from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('aboutus', view=views.aboutus, name='aboutus'),
    path('bloghome', view=views.bloghome, name='bloghome'),
    path('blogsingle', view=views.blogsingle, name='blogsingle'),
    path('category', view=views.category, name='category'),
    path('contact', view=views.contact, name='contact'),
    path('elements', view=views.elements, name='elements'),
    path('price', view=views.price, name='price'),
    path('search', view=views.search, name='search'),
    path('single', view=views.single, name='single'),
    path('signup', view=views.signup, name='signup'),
    path('login', view=views.login, name='login'),

]