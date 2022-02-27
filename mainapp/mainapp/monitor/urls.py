from django.urls import path
# from .views import *
from monitor import views
urlpatterns = [
    # path('api/upload/',views.UploadView.as_view(), name = 'prediction'),
    path('api/newupload/',views.newUpload.as_view(), name = 'new_upload'),
    path('api/checkidentity/',views.checkIdentity.as_view(), name = 'check_identity')
    # path('api/upload/ct', CTUploadView.as_view(), name = 'ct_prediction'),
]