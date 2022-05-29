from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('referanslar/', views.referanslar, name='referanslar'),
    path('news/', include('news.urls')),
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    path('', include('home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_news, name='category_news'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('faq/', views.faq_view, name='faq_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
