#from django.http import JsonResponse
import rest_framework
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

from .serializers import ProjectSerializer
from .serializers import Project, Review,Tag


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]

    #return JsonResponse(routes,  safe= False)
    return Response(routes)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getProjects(request):
    #print('USER : ', request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
    project = Project.objects.get(id = pk)
    serializer = ProjectSerializer(project, many=False)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project  = Project.objects.get(id= pk)
    user     = request.user.profile
    data     = request.data 
    print("data : ",data)

    review, created = Review.objects.get_or_create(
        owner = user,
        project = project,
    )

    review.value = data['value']
    review.body  = data['body']
    review.save()
    project.getVoteCount

    serializer = ProjectSerializer(project,many = False)
    
    return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']

    project = Project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)

    project.tags.remove(tag)

    return Response('Tag was deleted!')