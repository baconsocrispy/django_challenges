from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    name = models.CharField(max_length=60, null=False, default="")
    state = models.CharField(max_length=2, null=False, default="")
    campus_id = models.IntegerField(null=False)

    object = models.Manager()

    def __str__(self):
        display_campus = '{0.name}: {0.state}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campuses"
