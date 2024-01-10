from django.urls import path, register_converter, re_path

from blog.utils import FourDigitsYear
from blog.views import post_list, categories_list, post_details

register_converter(FourDigitsYear, "for_digits")
urlpatterns = [
    path('list/', post_list),
    path('details/<str:post_title>/', post_details),
    path('details/<int:post_id>/', post_details),
    path('details/<uuid:post_uuid>/', post_details),
    path('details/<slug:post_slug>/', post_details),
    path('details/<path:post_path>/', post_details),
    path('categories/list/', categories_list),
    path('archive/<for_digits:year>/', post_list),
    re_path(r'archive/(?P<year>[0-9]{2,4})/', post_list),
    path('archive/<for_digits:year>/<int:month>/', post_list),
    path('archive/<for_digits:year>/<int:month>/<int:day>/', post_list),
]
