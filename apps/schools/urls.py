from django.urls import path

from apps.schools import views


urlpatterns = [
    path('', views.login, name='index'),
      path('<int:id>/id/', views.id, name='id'),
    # ex: /polls/5/username/
    path('<varchar:username>/username/', views.username, name='username'),
    # ex: /polls/5/vote/
    path('<text:password>/password/', views.password, name='password'),

]

