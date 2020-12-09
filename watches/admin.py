from django.contrib import admin

from watches.models.watch import Watch
from watches.models.watch_description import WatchDescription

admin.site.register(Watch)
admin.site.register(WatchDescription)
