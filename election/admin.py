from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([AgentName, AnnouncedLgaResults,
                    AnnouncedPuResults, AnnouncedStateResults,
                    AnouncedWardResults, LGA, Party, PollingUnit,
                    State, Ward])
