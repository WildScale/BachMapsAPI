from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions, status
from Management.models import Etudiant,Adresse,Parent, Bus , Ecole, Notification, Chauffeur
from Management.serializers import EtudiantSerializer,AdresseSerializer,ParentSerializer,BusSerializer,EcoleSerializer,NotificationSerializer,ChauffeurSerializer
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.views import APIView
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return render_to_response('index.html')

class EtudiantViewSet(viewsets.ModelViewSet):
    queryset=Etudiant.objects.all()
    serializer_class=EtudiantSerializer


class AdresseViewSet(viewsets.ModelViewSet):
    queryset=Adresse.objects.all()
    serializer_class=AdresseSerializer
    

class ParentViewSet(viewsets.ModelViewSet):
    queryset=Parent.objects.all()
    serializer_class=ParentSerializer

class BusViewSet(viewsets.ModelViewSet):
    queryset=Bus.objects.all()
    serializer_class=BusSerializer

class EcoleViewSet(viewsets.ModelViewSet):
    queryset=Ecole.objects.all()
    serializer_class=EcoleSerializer

class ChauffeurViewSet(viewsets.ModelViewSet):
    queryset=Chauffeur.objects.all()
    serializer_class=ChauffeurSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer
