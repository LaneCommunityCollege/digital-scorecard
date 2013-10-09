from scorecard.models import Theme, Objective, Outcome, Indicator, StaticContent
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models


class ScoreCardAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 25, 'cols': 80})},
        models.CharField: {'widget': TextInput(attrs={'size': 60})},
    }

admin.site.register(Theme, ScoreCardAdmin)
admin.site.register(Objective, ScoreCardAdmin)
admin.site.register(Outcome, ScoreCardAdmin)
admin.site.register(Indicator, ScoreCardAdmin)
admin.site.register(StaticContent, ScoreCardAdmin)
