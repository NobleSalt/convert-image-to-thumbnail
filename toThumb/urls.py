from toThumb.views import UploadImage
from django.urls import path

app_name = 'thumb'
urlpatterns = [
    path('image/', UploadImage.as_view(), name='nail'),
]
