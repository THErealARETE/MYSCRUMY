from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse 
from  .models import *
# import datetime
from random import randint
from django.contrib.auth.models import User

def get_grading_parameters(request) :
      # return HttpResponse("This is a Scrum Application")
      goals = ScrumyGoals.objects.filter(goal_name = 'Learn Django')
      return HttpResponse(goals)



def move_goal(request, goal_id):
      display = ScrumyGoals.objects.get(goal_id = goal_id)
      return HttpResponse(display)

def add_goal(request):
      goalId = randint(1000, 9999)
      goalStatus = GoalStatus.objects.last()
      addGoalUser = User.objects.get(username = 'louis')
      addGoal = ScrumyGoals.objects.create(goal_name = 'keep learning django', goal_id = goalId, created_by = 'Louis' , moved_by = 'Louis', owner = 'Louis' , goal_status = goalStatus ,user = addGoalUser ) 
      return addGoal

def home (request):
     goals2 = ScrumyGoals.objects.filter(goal_name = 'keep learning django')
     return HttpResponse(goals2) 

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


# def learningDjango(request) :
     

 


# get_grading_parameters"Welcome to Django"