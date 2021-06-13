from django.urls import path
from . import views
from .views import ProfileUpdateView

urlpatterns = [
 path('', views.Index, name='index'),
 path('aboutus/', views.AboutPage, name='about'),
 path('dashboard/internship/e-logbook/', views.Dashboard, name='dashboard'),
 path('profile/internship/', views.Profile, name='profile'),
  path('profile/update/', ProfileUpdateView.as_view(), name='profile_edit'),
 path('internship/placement/detail/<intern_id>', views.Detail, name='detail'),
 path('search/', views.search, name='search'),
 path('employersLisT_placeEMent/', views.Employers_list, name='employers_list'),
 path('internship/ondo_placement/', views.OndoSearch, name='ondo_placement'),
 path('internship/lagos_placement/', views.LagosSearch, name='lagos_placement'),
 path('internship/abuja_placement/', views.AbujaSearch, name='abuja_placement'),
 path('internship/oyo_placement/', views.OyoSearch, name='oyo_placement'),

 path('dashboard/e-logbook/add_nEWlog', views.Addlog, name='add_log'),

]


from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
