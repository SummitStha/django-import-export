from django.conf.urls import url, include

from .views import (
	home, 
	exportCsv,
	exportJson,
	exportExcel,
	simple_upload
)

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^export-to-csv/$', exportCsv, name='export-csv'),
	url(r'^export-to-json/$', exportJson, name='export-json'),
	url(r'^export-to-excel/$', exportExcel, name='export-excel'),
    url(r'^import/$', simple_upload, name='import'),
]