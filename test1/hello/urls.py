from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello' ),
    # path('/<str:name>',views.greetings,name='greetings'),
    path('/coin',views.coin,name='coin'),

    # path('/vader',views.vader,name='vader'),
    # path('/starwars',views.starwars,name='starwars'),

]