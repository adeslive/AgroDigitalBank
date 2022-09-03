from django import forms

from .models import Bank



class BankModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.bank_name

class BankForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BankForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    select = BankModelChoiceField(queryset=Bank.objects.all(), label = 'Bank name')