"""
A set of classes representing hierarchy of promotions in a school.
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

class School(models.Model):
    """
    A School, contains login information.
    """
    name = models.CharField(max_length=80, verbose_name=_("Name"), )
    hruid = models.SlugField(max_length=20, unique=True, verbose_name=_("Unique slug identifier"))
    suffix = models.SlugField(max_length=50, unique=True, verbose_name=_("Email suffix of the school"))
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _("school")
        verbose_name_plural = _("schools")

    def __str__(self):
        return self.name

class Formation(models.Model):
    """
    A formation inside a School.
    """
    name = models.CharField(max_length=80,verbose_name=_("Name"))
    hruid = models.SlugField(max_length=20, unique=True, verbose_name=_("Unique slug identifier"))
    description = models.TextField(verbose_name=_("Description"))
    school = models.ForeignKey(School, related_name='formations', verbose_name=_("Related school"))

    class Meta:
        verbose_name = _("formation")
        verbose_name_plural = _("formations")

    def __str__(self):
        return self.name

class Promotion(models.Model):
    """
    A promotion of a Formation.
    """
    year = models.IntegerField(verbose_name=_("Year"))
    formation = models.ForeignKey(Formation, related_name='promotions', verbose_name=_("Related formation"))

    class Meta:
        verbose_name = _("promotion")
        verbose_name_plural = _("promotions")

    def __str__(self):
        return "Promotion %(self.year)i of %(self.formation.name)" % self

