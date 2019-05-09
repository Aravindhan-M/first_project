from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.conf import settings
from django.contrib.auth.models import Group

from mailsnake import MailSnake

User = get_user_model()
ms = MailSnake(settings.MAILCHIMP_API_KEY)
list_id = settings.MAILCHIMP_EMAIL_LIST_ID


class UserAdmin(admin.ModelAdmin):
    list_display = ('mobile_number', 'email', 'get_full_name', 'is_active')


# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:

        model = Group
        exclude = ['permissions']

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
         queryset=User.objects.all(),
         required=False,
         # Use the pretty 'filter_horizontal widget'.
         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()

        # for adding the users to the list of mailchimp susbscribers group
        for user in instance.user_set.all():
            result = ms.listSubscribe(id=list_id,
                                      email_address=user.email,
                                      update_existing=True, double_optin=False)
        # Save many-to-many data
        self.save_m2m()
        return instance






# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    #filter_horizontal = ['permissions']


# Unregister the original Group admin.
admin.site.unregister(Group)

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
admin.site.register(User,UserAdmin)