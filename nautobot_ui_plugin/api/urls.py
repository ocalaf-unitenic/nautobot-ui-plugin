from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.APIRootView = views.NautobotUIPluginRootView

router.register(r'nautobotsavedtopologies', views.NautobotSavedTopologyViewSet)

app_name = "nautobot_ui_plugin-api"
urlpatterns = router.urls
