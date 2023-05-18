from django.forms import ModelForm
from .models import Agent, Listing

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = [
            'name',
            'photo',
            'about',
            'phone',
            'mobile',
            'email',
            'skype',
            'telegtam',
            'whatsapp',
            'viber'
        ]


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
