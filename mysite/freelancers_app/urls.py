from django.urls import path,include
from rest_framework import routers
from .views import (SkillViewSet,UserProfileViewSet,SocialNetworkViewSet,CategoryViewSet,
                    ProjectViewSet,OfferViewSet,ReviewViewSet)


router=routers.SimpleRouter()
router.register(f'users',UserProfileViewSet,basename='users')
router.register(f'skill',SkillViewSet,basename='skill')
router.register(f'social_network',SocialNetworkViewSet,basename='social_network')
router.register(f'category',CategoryViewSet,basename='category')
router.register(f'review',ReviewViewSet,basename='review')
router.register(f'project',ProjectViewSet,basename='project')
router.register(f'offer',OfferViewSet,basename='offer')

urlpatterns= [
    path('',include(router.urls)),]