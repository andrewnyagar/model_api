from django.forms import ModelForm
from .models import Turnover


class TurnoverForm(ModelForm):
    class Meta:
        model = Turnover
        fields = '__all__'