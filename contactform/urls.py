from django.urls import path
from . import views

urlpatterns = [
    path('contact/submit/' , views.contact_add , name = 'contact_add'),
    path('panel/contact_form/' , views.contact_show , name = 'contact_show'),
    path('panel/contact_del/<int:pk>' , views.contact_del , name = 'contact_del'),
]
