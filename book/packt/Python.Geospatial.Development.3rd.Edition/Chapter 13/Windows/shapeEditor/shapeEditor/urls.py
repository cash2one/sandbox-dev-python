from django.conf.urls import include, url
from django.contrib.gis import admin
import shapeEditor.shapefiles.views
import shapeEditor.tms.urls

urlpatterns = [
    url(r'^$', shapeEditor.shapefiles.views.list_shapefiles),
    url(r'^import$', shapeEditor.shapefiles.views.import_shapefile),
    url(r'^export/(?P<shapefile_id>\d+)$',
            shapeEditor.shapefiles.views.export_shapefile),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tms/', include(shapeEditor.tms.urls)),
    url(r'^edit/(?P<shapefile_id>\d+)$',
        shapeEditor.shapefiles.views.edit_shapefile),
    url(r'^find_feature$', shapeEditor.shapefiles.views.find_feature),
    url(r'^edit_feature/(?P<shapefile_id>\d+)/(?P<feature_id>\d+)$',
        shapeEditor.shapefiles.views.edit_feature),
    url(r'^edit_feature/(?P<shapefile_id>\d+)$',
        shapeEditor.shapefiles.views.edit_feature),
    url(r'^delete_feature/(?P<shapefile_id>\d+)/(?P<feature_id>\d+)$',
        shapeEditor.shapefiles.views.delete_feature),
    url(r'^delete/(?P<shapefile_id>\d+)$',
        shapeEditor.shapefiles.views.delete_shapefile),

]
