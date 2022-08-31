from django.contrib import admin
from dormitory.models import Dormitory
from dormitory.models import Question
from dormitory.models import Answer 


admin.site.register(Dormitory)
admin.site.register(Question)
admin.site.register(Answer)