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

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from lck.django.activitylog.admin import UserIPInline, UserAgentInline

from mudmafia.app.models import Profile


from django_evolution.models import Version as _Version, Evolution as _Evolution
admin.site.unregister(_Version)
admin.site.unregister(_Evolution)
del _Version
del _Evolution


class ProfileInline(admin.StackedInline):
    model = Profile
    readonly_fields = ('last_active',)


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline, UserIPInline, UserAgentInline]

    def nick(self):
        return self.get_profile().nick
    nick.admin_order_field = 'profile__nick'

    def birth_date(self):
        return self.get_profile().birth_date
    birth_date.short_description = _("birth date")
    birth_date.admin_order_field = 'profile__birth_date'

    def groups_show(self):
        return "<br> ".join([g.name for g in self.groups.order_by('name')])
    groups_show.allow_tags = True
    groups_show.short_description = _("groups")


    search_fields = ('username', 'first_name', 'last_name',
        'email', 'profile__nick')
    list_display = ('username', 'email', 'first_name', 'last_name',
        groups_show, 'is_staff', 'is_active')
    list_filter = ('groups',)

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
