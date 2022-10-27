from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.userProfile, name='profile'),
    path('top10/', views.top10, name='top10'),

    path('user-account/', views.userAccount, name='user-account'),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('add-experience/', views.createExperience, name="add-experience"),
    path('update-experience/<str:pk>', views.updateExperience, name="update-experience"),
    path('delete-experience/<str:pk>', views.deleteExperience, name="delete-experience"),
    path('add-education/', views.createEducation, name="add-education"),
    path('update-education/<str:pk>', views.updateEducation, name="update-education"),
    path('delete-education/<str:pk>', views.deleteEducation, name="delete-education"),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>', views.viewMessage, name="message"),
    path('send-message/<str:pk>', views.sendMessage, name="send-message"),
]