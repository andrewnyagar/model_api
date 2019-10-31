from rest_framework import serializers
from predictor.models import Turnover


class TurnoverSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Turnover
        fields = "__all__"