from django.urls import path, include
from django.views.generic.base import TemplateView

from django.contrib import admin

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    # path("", squad.views.index, name="index"),
    # path("db/", hello.views.db, name="db"),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('search/', include('squad.urls')),

]
