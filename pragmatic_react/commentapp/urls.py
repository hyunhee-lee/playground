from django.urls import path


from commentapp.views import CommentCreateView, CommentDeleteView


from django.conf.urls import url, include
from django.contrib import admin
from commentapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', views.CommentViewSet)


app_name = 'commentapp'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),

    # path('create/', CommentCreateView.as_view(), name='create'),
    # path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]