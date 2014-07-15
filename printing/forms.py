from datetime import date, timedelta
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
import re

PHONE_NUMBER_REGEX = re.compile(r'^[+]?((\d+[\s]?[-]?\d+)+)$')

class PhoneNumberField(forms.RegexField):
    def __init__(self, *args, **kwargs):
        kwargs['regex'] = PHONE_NUMBER_REGEX
        kwargs['max_length'] = 15
        kwargs['min_length'] = 10
        kwargs['error_messages'] = {
                'invalid' : "Invalid phone Number",
                'required': "Required phone number"
            }
        super(PhoneNumberField, self).__init__(*args, **kwargs)

class UserForm(forms.Form):
    """
    A form that creates a user reseller, from the given domain and password.
    """
    company= forms.CharField(label=_("Company or Organization"),
                             error_messages={'required':"user id field required"},required=False)
    name = forms.CharField(label=_("Name"), max_length=45,widget=forms.TextInput(attrs={'placeholder': 'name'}),
                               error_messages={'required':"name field is required"},required=True)
    #password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput,
                                error_messages={'required':"Password field required"},required=False)
    #password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
                                error_messages={'required':"Retype Password field required"},required=False)
    email = forms.EmailField(label=_("Email"),
                             help_text=_("An auto generated mail will be sent to confirm email id"),
                             error_messages={'required':"Email field required"},required=True)
    contact_number = PhoneNumberField(label='Phone number',error_messages={'required':"Phone Number required"},required=True)
    #address = forms.CharField(label=_("Address"), max_length=140,error_messages={'required':"Address required"},required=True)
    user_active = forms.ChoiceField(label=_("User Status"),choices=[("True", "Enabled"),("False", "Disabled")])
    address = forms.CharField(label=_("Address"),widget=forms.Textarea,required=True)
    pincode

    expiry_date = forms.DateTimeField(initial=(date.today() + timedelta(days=180)).isoformat(),
                                    label=_("Expiry Date"),required=False)
    plan_active = forms.ChoiceField(label=_("Emergency Number Status"),choices=[("True", "Enabled"),("False", "Disabled")])
    plan_number = forms.CharField(required=False, label='Emergency Number',
                                                  #widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}),
                                                  error_messages={'required':"Please choose at least one product"})
    is_distributor = forms.ChoiceField(label=_("Is Distrtibutor"),choices=[("True", "Yes"),("False", "No")], required=False, initial = "False")


    def __init__(self, user=None, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        try:
            site = Site.objects.get(id=settings.SITE_ID)
        except:
            pass
        

    def clean_plan_number(self):
        plan_number = self.cleaned_data.get("plan_number",None)
        if not plan_number:
            raise forms.ValidationError("Please select atleast one emergency number")
        return plan_number
    
    def clean_user_id(self):
        user_id = self.cleaned_data.get("user_id", None)
        return user_id

    def clean_username(self):
        username = self.cleaned_data.get("username",None)
        user_id = self.cleaned_data.get("user_id", None)
        if not username:
            raise forms.ValidationError(_("Invalid user name."))
        username = username.strip()
        if username=="":
            raise forms.ValidationError(_("Invalid user name."))

        if user_id:
            count = User.objects.filter(username=username, site__id=settings.SITE_ID).exclude(id=user_id).count()
        else:
            count = User.objects.filter(username=username,site__id=settings.SITE_ID).count()
        if count>0:
            raise forms.ValidationError(_("User name already exist."))
        return username


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1",None)
        password2 = self.cleaned_data.get("password2",None)
        user_id = self.cleaned_data.get("user_id",None)
        password1 = password1.strip()
        if not user_id:
            if password2 == "":
                raise forms.ValidationError("Invalid password.")
            if password1 != password2:
                raise forms.ValidationError("The two passwords fields didn't match.")
        else:
            if password1 != password2:
                raise forms.ValidationError("The two passwords fields didn't match.")
            elif password2 == "":
                return None
        return password2

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email:
            raise forms.ValidationError(_("Email address is required."))
        else:
            return self.validate_email(email)

    def validate_email(self, email):
        user_id = self.cleaned_data.get("user_id", None)
        try:
            tempuser = User.objects.get(email=email, site__id=settings.SITE_ID)
        except User.DoesNotExist:
            return email
        if tempuser.id == user_id:
            return email
        raise forms.ValidationError(_("Email address already exist."))

