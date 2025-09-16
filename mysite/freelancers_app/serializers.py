from .models import *
from rest_framework import serializers

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields='__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['first_name','last_name']

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model=SocialNetwork
        fields='__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','category_name']

class OfferSerializer(serializers.ModelSerializer):
    freelancer=UserRoleSerializer()
    class Meta:
        model=Offer
        fields=['freelancer','proposed_budget','proposed_deadline','created_date']


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['id','title','budget','description']

class ProjectDetailSerializer(serializers.ModelSerializer):
    client=UserRoleSerializer()
    offer=OfferSerializer(many=True, read_only=True)
    comment=Review()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model=Project
        fields=['title','budget','description','deadline','status',
                'skills_required','created_date','client','offer','comment']

class CategoryDetailSerializer(serializers.ModelSerializer):
    project=ProjectListSerializer(many=True,read_only=True)

    class Meta:
        model=Category
        fields=['category_name','project']


class ReviewSerializer(serializers.ModelSerializer):
    reviewer=UserRoleSerializer()
    class Meta:
        model=Review
        fields=['reviewer','rating','comment','created_date']

