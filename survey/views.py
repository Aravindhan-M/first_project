
from django.shortcuts import render
from .models import Survey, SurveyedUsers
from django.http import Http404, JsonResponse

def index(request):
    survey = Survey.objects.filter(active=True)[0]
    if SurveyedUsers.objects.filter(surveyed_by=request.user, survey=survey).exists():
        return JsonResponse({"status":False})
    return JsonResponse({"status":True,"survey_url":survey.survey_url})
