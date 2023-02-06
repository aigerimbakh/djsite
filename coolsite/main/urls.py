from django.urls import path
from .views import *

urlpatterns = [
 path('', index)
]

handler404 = pageNotFound
handler403 = HttpResponseForbidden
handler400 = HttpResponseBadRequest
handler500 = HttpResponseServerError