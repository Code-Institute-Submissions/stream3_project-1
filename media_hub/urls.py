"""media_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from home import views as home_views
from paypal.standard.ipn import urls as paypal_urls
from payment import views as paypal_views
from products import views as product_views
from accounts.views import register, account, login, logout
from orders import views as order_views 
from contact.views import contact


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', home_views.get_index),
    url(r'^about/$', home_views.about, name='about'),
    
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),

    url(r'^contact/', contact, name='contact'),

    #User URLS
    url(r'^register/$', register, name='register'),
    url(r'^account/$', account, name='account'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    #Paypal URLS 
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^payment/', include('payment.urls', namespace='payment')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),


    # Product URLS 
    url(r'^products/$', product_views.all_products, name='products'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_views.product_detail, name='product_detail'),
    url(r'^download/(?P<order_id>\d+)/(?P<product_id>\d+)/$', order_views.download, name='download'), # view a purchase
    
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))

    