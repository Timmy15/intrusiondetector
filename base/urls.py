from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),


    # path('', views.home, name="home"),
    path('attack/<int:form_id>/', views.attack, name='attack_view'),
    path('attack/', views.attack, name="attack"),
    path('results/<int:form_id>/', views.results, name='results_view'),
    path('results/', views.results, name="results"),

    path('predict_dos/', views.predict_dos, name="predict_dos"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('labels/', views.labelsPage, name='labelsPage'),
    path('delete-form/<str:pk>/', views.deleteForm, name="delete-form"),
    # path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('labels/', views.labelsPage, name="labels"),
    # path('activity/', views.activityPage, name="activity"),
]