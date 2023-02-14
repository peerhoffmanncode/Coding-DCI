from django.contrib import admin
from .models import NewStats


from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from .models import NewStats

import json


@admin.register(NewStats)
class NewStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        stat_data = NewStats.objects.annotate().values("win", "mac", "linux", "other")

        # data = NewStats.objects.all()
        # newdata = serializers.serialize(
        #     "json", list(data), fields=("win", "mac", "linux", "other")
        # )
        # print(newdata)

        as_json = json.dumps(list(stat_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"stat_data": as_json}

        return super().changelist_view(request, extra_context=extra_context)
