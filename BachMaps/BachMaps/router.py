from Management.views import *
from rest_framework import routers


router=routers.DefaultRouter()
router.register('etudiants',EtudiantViewSet)
router.register('adresses',AdresseViewSet)
router.register('bus',BusViewSet)
router.register('chauffeurs',ChauffeurViewSet)
router.register('ecoles',EcoleViewSet)
router.register('notifications',NotificationViewSet)
router.register('parents',ParentViewSet)

