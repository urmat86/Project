from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from .views import (SkillViewSet,UserProfileViewSet,SocialNetworkViewSet,CategoryListAPIView,CategoryDetailAPIView,
                    ProjectListAPIView,ProjectDetailAPIView,OfferViewSet,ReviewViewSet)


router=routers.SimpleRouter()
router.register(f'users',UserProfileViewSet,basename='users')
router.register(f'skill',SkillViewSet,basename='skill')
router.register(f'social_network',SocialNetworkViewSet,basename='social_network')
router.register(f'review',ReviewViewSet,basename='review')
router.register(f'offer',OfferViewSet,basename='offer')

urlpatterns= [
    path('',include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category'),
    path('category/<int:pk>/',CategoryDetailAPIView.as_view(),name='category_detail'),
    path('project/', ProjectListAPIView.as_view(), name='project'),
    path('project/<int:pk>/',ProjectDetailAPIView.as_view(),name='project_detail'),

]