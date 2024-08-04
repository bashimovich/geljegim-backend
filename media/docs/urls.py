from django.urls import path, include
from rest_framework import routers
from . import views as api_viewset
from . import views
from django.conf import settings  # ADDED
from django.conf.urls.static import static  # ADDE

router = routers.DefaultRouter()
# parent routes
router.register(r'main-banner', api_viewset.BannerMainViewSet, basename="main-banner")
router.register(r'side-banner', api_viewset.SideBannerViewSet, basename="side-banner")
router.register(r'categories', api_viewset.CategoryViewSet, basename="categories")
router.register(r'articles', api_viewset.ArticlesViewSet, basename="articles")

#child routes 
router.register(r'marque-articles', api_viewset.MarqueArticlesViewSet, 
    basename="marque-articles")

router.register(r'main-article', api_viewset.MainArticlesViewSet, 
    basename="main-article")

router.register(r'four-article', api_viewset.FourArticlesViewSet, 
    basename="four-article")

router.register(r'multimedia-article', api_viewset.MultimediaArticlesViewSet, 
    basename="multimedia-article")

router.register(r'homeuniver-article', api_viewset.HomeUniverArticlesViewSet, 
    basename="homeuniver-article")
router.register(r'univer-article', api_viewset.UniverArticlesViewSet, 
    basename="univer-article")
router.register(r'homevacational-article', api_viewset.HomeVacationalArticlesViewSet, 
    basename="homevacational-article")
router.register(r'vacational-article', api_viewset.VacationalArticlesViewSet, 
    basename="vacational-article")
router.register(r'official-article', api_viewset.OfficialArticlesViewSet, 
    basename="official-article")

urlpatterns = [
    path(r'', include(router.urls)),
    path('articles/via/<str:typear>/', views.ArticlesViaTypearViewSet.as_view({'get': 'list'}), name='article-typear'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

