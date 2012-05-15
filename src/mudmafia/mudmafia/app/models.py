#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 by Łukasz Langa
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models as db
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from lck.django.activitylog.models import MonitoredActivity
from lck.django.common.models import TimeTrackable, EditorTrackable, Named
from lck.django.profile.models import BasicInfo, ActivationSupport,\
        GravatarSupport


class Profile(BasicInfo, ActivationSupport, GravatarSupport,
        MonitoredActivity):
    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __unicode__(self):
        return self.nick


class LicenseType(Named, TimeTrackable, EditorTrackable):
    class Meta:
        verbose_name = _("license type")
        verbose_name_plural = _("license types")

    def get_editor_from_request(self, request):
        return request.user.get_profile()



class License(TimeTrackable, EditorTrackable):
    name = db.CharField(_("name"), max_length=100)
    description = db.TextField(_("description"))
    license_type = db.ForeignKey(LicenseType,
        verbose_name=_("license type"))
    issue_date = db.DateField(_("issue date"))
    valid_for = db.PositiveIntegerField(_("valid for"),
        default=30, help_text=_("In days."))

    class Meta:
        verbose_name = _("license")
        verbose_name_plural = _("licenses")

    def __unicode__(self):
        return self.name

    def get_editor_from_request(self, request):
        return request.user.get_profile()


@receiver(db.signals.post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        profile, new = Profile.objects.get_or_create(user=instance)
