"""
The classes representing the differents groups (binets, sports, groups, etc.)
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import * 

class Group(models.Model):
    """
    A group
    """
    TYPE_CHOICES = ( ("bin", "binet"), ("grp", _("group")), ("spo", _("sport")), ("cls", _("class")) )
    
    name = models.CharField(max_length=80, verbose_name=_("Name"), )
    hruid = models.SlugField(max_length=20, unique=True, verbose_name=_("Unique slug identifier"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to="group_images/", verbose_name=_("Group image"), blank=True, null=True)
    email_prefix = models.CharField(max_length=80, verbose_name=_("Email prefix"), blank=True, null=True)
    wikix_page = models.CharField(max_length=80, verbose_name=_("Link to wikix page"), blank=True, null=True)
    web_page = models.CharField(max_length=255, verbose_name=_("Web page address"), blank=True, null=True, validators=[URLValidator()])
    group_type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")

    def __str__(self):
        return self.name

class GroupMember(models.Model):
    """
    A member of a group (used in a M2M relation)
    """
    STATUS_CHOICES = ( ("sym", _("sympathizer")), ("mem", _("member")), ("adm", _("administrator")))

    student = models.ForeignKey("students.Student",verbose_name=_("Student"))
    group = models.ForeignKey("Group", verbose_name=_("Group"))
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    visible = models.BooleanField(default=True)
    message = models.TextField(verbose_name=_("Custom message"))

    class Meta:
        verbose_name = _("Membership relation")
        verbose_name_plural = _("Membership relations")

    def __str__(self):
        return "%s -> %s " % (self.student, self.group)
