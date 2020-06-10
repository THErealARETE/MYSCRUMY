# from django.urls import path
# from benpelumiscrumy import views


# urlpatterns = [
#     path('', views.homePage, name='home'),
# ]

from django.urls import path,include
# from .views import homePage
from benpelumiscrumy import views


app_name = 'benpelumiscrumy'
urlpatterns = [
     path( '', views.index,name = 'index' ),
     path('movegoal/<int:goal_id>', views.move_goal, name = 'moveGoal'),
     path('addgoal/',views.add_goal, name = 'addGoal'),
     # path(r'^drinks/<str:drink_name>/',TemplateView.as_view(template_name='drinks/index.html'),name="drink")
     # path('addgoal/', views.move_goal.as_view(template_name = 'benpelumiscrumy/addGoal.html') , name= 'addGoal'),
     path('home/',views.home, name = 'home' ),
     path('homealone/<int:goal_id>', views.homealone),
     path('accounts/', include('django.contrib.auth.urls'), name = 'accounts')
]


    