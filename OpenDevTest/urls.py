from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from testapp import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'book-themes', views.BookThemeViewSet)
router.register(r'readers', views.ReaderViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'book-ordered', views.BookOrderedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls',
                             namespace='rest_framework'))
]
