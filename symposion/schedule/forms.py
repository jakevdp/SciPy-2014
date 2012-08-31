from django import forms

from symposion.schedule.models import Slot, Presentation


class SlotEditForm(forms.Form):
    
    presentation = forms.ModelChoiceField(
        queryset=Presentation.objects.filter(slot__isnull=True),
        required=True,
    )
