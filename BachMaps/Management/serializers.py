from Management.models import Etudiant,Adresse ,Parent, Bus, Chauffeur , Ecole , Notification
from rest_framework import serializers


class EtudiantSerializer(serializers.ModelSerializer):
    class Meta :
        model=Etudiant
        fields='__all__'

class AdresseSerializer(serializers.ModelSerializer):

    class Meta:
        model=Adresse
        fields='__all__'

class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Parent
        fields='__all__'

class BusSerializer(serializers.ModelSerializer):

    class Meta:
        model=Bus
        fields='__all__'

class ChauffeurSerializer(serializers.ModelSerializer):

    class Meta:
        model=Chauffeur
        fields='__all__'

class EcoleSerializer(serializers.ModelSerializer):

    class Meta:
        model=Ecole
        fields='__all__'


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Notification
        fields='__all__'

