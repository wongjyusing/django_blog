from rest_framework import routers
from back_end.api_views import BlogViewSet
router = routers.DefaultRouter()
router.register(r'dd', BlogViewSet)
