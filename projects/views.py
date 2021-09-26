#from projects.utils import searchProjects

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm,ReviewForm
from django.contrib import messages

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .utils import searchProjects,paginateProjects

# Create your views here.

projectsList = [
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':'Portfolio Website',
        'description':'This was a project where I built out my portfolio'    
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'Awsome open source project I am still working on'    
    },

]

msg = "projects/dynamic value"
number = 10
context = {'page':msg,'number':number,'projects':projectsList}

def projects(request):
    projects,search_query = searchProjects(request)
    
    custom_range, projects, paginator = paginateProjects(request, projects,6)
    #project = Project.objects.all()
    context = {'projects':projects,"search_query":search_query, 'custom_range':custom_range, 'paginator':paginator,}
    return render(request,'projects/projects.html',context)


def project(request,pk):
    '''projectObj = None
    for item in projectsList:
        if item['id'] == pk:
            projectObj = item'''
    
    projectObj = Project.objects.get(id = pk)
    #tags = projectObj.tags.all()    #-- can use this in template(single_page.html) rather than here. 
            # also exclude {'tags':tags}

    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner   = request.user.profile
        review.save()
        
    #update project vote count

        projectObj.getVoteCount
        messages.success(request,'Your review was successfully submitted')
        return redirect('project', pk = projectObj.id)
    
    return render(request,'projects/single-project.html',{'projectObj':projectObj,'project':projectObj,'form':form})

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        #print(request.POST)
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        form = ProjectForm(request.POST,request.FILES)
        #print(form)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name= tag)
                project.tags.add(tag)

            return redirect('account')

    context = {'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def updateProject(request,pk):
    profile = request.user.profile
    
    project = profile.project_set.get(id = pk)
    
    #project = Project.objects.get(id = pk)
    form = ProjectForm(instance = project)
    if request.method == 'POST':
        #print(request.POST)
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        
        #tag  = Tag.objects.create(name=newtags)
        
        form = ProjectForm(request.POST,request.FILES,instance=project)
        #print(form)
        if form.is_valid():
            project = form.save()
            
            #project.tags.add(tag)  linked to line 104
            
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name= tag)
                project.tags.add(tag)

            return redirect('account')

    context = {'form':form,'project':project}
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def deleteProject(request,pk):
    profile = request.user.profile
    form = profile.project_set.get(id = pk)
    #form = Project.objects.get(id = pk)

    if request.method == 'POST':
        #if form.is_valid():
            form.delete()
            return redirect('projects')


    context = {"object":form}
    return render(request,'delete_template.html',context)
