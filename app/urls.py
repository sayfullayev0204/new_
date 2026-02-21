from django.urls import path
from .views import home,news_detail,devon,leadership,news,olimpiada,yunalish_list, yunalish_detail
urlpatterns = [
    path('', home, name='home'),
    path('news_detail/<int:pk>', news_detail, name='news_detail'), 
    path('devon/', devon, name='devon'), 
    path('leadership/', leadership, name='leadership'), 
    path('gazal/', news, name='news'),  
    path('personal/', olimpiada, name='olimpiada'),
    path('<int:pk>', yunalish_list, name='yunalish_list'),  
    path('detail/<int:pk>', yunalish_detail, name='yunalish_detail'),
]