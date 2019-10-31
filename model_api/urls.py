from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from predictor.views import TurnoverViewset

router = routers.DefaultRouter()
router.register("predictor", TurnoverViewset)

urlpatterns = [path('admin/', admin.site.urls), path("", include(router.urls))]
