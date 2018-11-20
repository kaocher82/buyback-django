from rest_framework.routers import SimpleRouter

from .api import InspectionViewSet


router = SimpleRouter()

router.register(r'inspections', InspectionViewSet)

urlpatterns = router.urls
