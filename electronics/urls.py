 
 
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from.import productviews
from . import views
from . import adminview
from . import pbview
from .import userviews
from .import userproductviews

urlpatterns = [
    path('deviceinterface/', views.device_interface),
    path('devicesubmit', views.device_submit),
    path('devicedisplay/', views.device_display),
    path('displaybyid/', views.device_display_id),
    path('editdeletedevice', views.device_edit_delete),
    path('adminlogin/', adminview.admin_login),
    path('checkadminlogin/', adminview.check_admin_login),
    path('product/', productviews.product_interface),
    path('productsubmit', productviews.product_submit),
    path('productdisplay/', productviews.product_display),
    path('displaybyproductid/', productviews.product_display_id),
    path('editdeleteproduct', productviews.product_edit_delete),
    path('showUserInterface/',userviews.showUserInterface),
    path('usersubmit/',userviews.submituser),
    path('userLogin/',userviews.userLogin),
    path('checkUserLogin/',userviews.checkUserLogin),
    path('userProduct/',userproductviews.showUserProduct),
    path('submitUserProduct/',userproductviews.submitUserProduct),
    path('onoffinterface/', pbview.onoff_interface),
    path('onoff/', pbview.on_off),
]
urlpatterns+=staticfiles_urlpatterns()
