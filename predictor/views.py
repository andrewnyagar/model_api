from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TurnoverSerializer
from .models import Turnover
from .forms import TurnoverForm
from django.contrib import messages

from .model_pkl import attrition_model
from django.contrib.auth.decorators import login_required


# Create your views here.
class TurnoverViewset(viewsets.ModelViewSet):
    queryset = Turnover.objects.all()
    serializer_class = TurnoverSerializer

@login_required
def PostData(request):
    if request.method == "POST":
        form = TurnoverForm(request.POST)
        if form.is_valid():
            form.save()
            result = attrition_model.getData(form.cleaned_data)
            if (result == 0):
                messages.success(request, f'No Turnover {result}')
            else:
                messages.success(request, f'Turnover')
            # return redirect("")
    else:
        form = TurnoverForm()
    return render(request, 'predictor/index.html', {'form': form})