from django.urls import path


from profileapp.views import ProfileCreateView, ProfileUpdateView


from django.conf.urls import url, include
from django.contrib import admin
from profileapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', views.ProfileViewSet)


app_name = 'profileapp'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),

    # path('create/', ProfileCreateView.as_view(), name='create'),
    # path('update/<int:pk>', ProfileUpdateView.as_view(), name='update')
]