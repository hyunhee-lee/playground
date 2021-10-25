from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView
# from articleapp.views import ArticleListView


from django.conf.urls import url, include
from django.contrib import admin
from articleapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', views.ArticleViewSet)


app_name = 'articleapp'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),

    # # path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    # path('list/', ArticleListView.as_view(), name='list'),
    #
    # path('create/', ArticleCreateView.as_view(), name='create'),
    # path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    # path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]