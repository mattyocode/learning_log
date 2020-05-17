from django.shortcuts import render

# Create your views here.
def index(request):
    '''The home page for Learning Log'''
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''show all topics'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learnings_logs/topics.html', context)