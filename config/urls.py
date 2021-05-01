
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_login.urls')),
    path('blog/', include('App_Blog.urls')),
    path('',views.index,name='index'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

