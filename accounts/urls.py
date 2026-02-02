from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('librarian/dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
    path('member/dashboard/', views.member_dashboard, name='member_dashboard'),
]
