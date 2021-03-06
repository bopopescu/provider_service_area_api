"""provider_service_area_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers, schemas, renderers, response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from provider.views import ProviderViewSet
from service_area.views import ServiceAreaViewSet


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer, renderers.CoreJSONRenderer])
def schema_view(request):
    """
    Auto API Documentation
    """
    generator = schemas.SchemaGenerator()
    return response.Response(generator.get_schema(request=request))


router = routers.DefaultRouter()
router.register(r'providers', ProviderViewSet, base_name='providers')
router.register(r'service-areas', ServiceAreaViewSet, base_name='service-areas')

urlpatterns = router.urls
urlpatterns.append(url(r'docs/', schema_view),)

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
