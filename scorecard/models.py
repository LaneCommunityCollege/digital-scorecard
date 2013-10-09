from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Theme(models.Model):
    themeid = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    score = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1, validators=[MaxValueValidator(4), MinValueValidator(1)])
    foundation = models.BooleanField(default=False, help_text="Used to mark this theme as the the underlying foundation (usually false)")

    def save(self):
        # Makes sure that there isn't more than one foundation theme
        if self.foundation:
            try:
                temp = Theme.objects.get(foundation=True)
                if self != temp:
                    raise forms.ValidationError("There can only be one foundation theme")
            except Theme.DoesNotExist:
                pass
        super(Theme, self).save()

    def sorted_objectives(self):
        return self.objective_set.all().extra(order_by=['objectiveid'])

    def __unicode__(self):
        return "%s - %s" % (self.themeid, self.name)


class Objective(models.Model):
    objectiveid = models.IntegerField()
    theme = models.ForeignKey(Theme)
    name = models.CharField(max_length=255)
    score = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1, validators=[MaxValueValidator(4), MinValueValidator(1)])
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('objectiveid', 'theme')

    def sorted_outcomes(self):
        return self.outcome_set.all().extra(order_by=['outcomeid'])

    def __unicode__(self):
        return "%s.%s - %s" % (self.theme.themeid, self.objectiveid, self.name)


class Outcome(models.Model):
    outcomeid = models.IntegerField()
    objective = models.ForeignKey(Objective)
    name = models.CharField(max_length=255)
    score = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1, validators=[MaxValueValidator(4), MinValueValidator(1)])
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('outcomeid', 'objective')

    def sorted_indicators(self):
        return self.indicator_set.all().extra(order_by=['indicatorid'])

    def __unicode__(self):
        return "%s.%s.%s - %s" % (self.objective.theme.themeid, self.objective.objectiveid, self.outcomeid, self.name)


class Indicator(models.Model):
    indicatorid = models.IntegerField()
    outcome = models.ForeignKey(Outcome)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    score = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1, validators=[MaxValueValidator(4), MinValueValidator(1)])

    class Meta:
        unique_together = ('indicatorid', 'outcome')

    def __unicode__(self):
        return "%s.%s.%s.%s - %s" % (self.outcome.objective.theme.themeid, self.outcome.objective.objectiveid, self.outcome.outcomeid, self.indicatorid, self.name)


class StaticContent(models.Model):
    pageurl = models.CharField(max_length=64)
    pagetitle = models.CharField(max_length=255)
    pagebody = models.TextField()

    def __unicode__(self):
        return self.pagetitle
