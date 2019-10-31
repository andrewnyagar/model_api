from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from predictor.views import TurnoverViewset
from users import views as user_views
from django.contrib.auth import views as auth_views
from predictor.views import PostData



router = routers.DefaultRouter()
router.register("predictor", TurnoverViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("register/", user_views.register, name="register"),
    path("post/", PostData, name="post"),
    # path("login/", auth_views.register, name="register"),
]
