from django.contrib import admin
from .models import Adresse
from .models import Notification
from .models import Ecole
from .models import Chauffeur
from .models import Bus
from .models import Etudiant
from .models import Parent
# Register your models here.

admin.site.register(Adresse)
admin.site.register(Notification)
admin.site.register(Ecole)
admin.site.register(Chauffeur)
admin.site.register(Bus)
admin.site.register(Etudiant)
admin.site.register(Parent)

