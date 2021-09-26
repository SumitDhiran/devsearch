from rest_framework import serializers
from projects.models import Project,Review,Tag
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__' 


class ProjectSerializer(serializers.ModelSerializer):
    owner  = ProfileSerializer(many = False)
    tags = TagSerializer(many = True)
    #reviews = ReviewSerializer(many = True)    ~ wont work since reviews is not an attribute of Project class, its a child class
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'

    def get_reviews(self,obj):  # obj refers to the object we are serializing, ie. object of Project class that we are serializing
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many = True)
        return serializer.data