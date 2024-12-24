from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

#@login_required
def topics(request):
    """显示所有的主题"""
    
    # 先将所有公开主题放入
    publicTopics = Topic.objects.filter(public = True)
    
    # 判断是否登录
    if request.user.is_authenticated:
        userTopics = Topic.objects.filter(owner = request.user)
        # 将public为True的公开主题也加进来
        topics = (userTopics | publicTopics).order_by('-date_added')
        
    # 若是未登录，只展示公开主题
    else:
        topics = publicTopics
        
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

#@login_required
def topic(request, topic_id):
    """显示单个主题以及其所有的条目"""
    topic = Topic.objects.get(id = topic_id)
    
    # 如果是公开主题，就不验证用户
    if topic.public != True:
        check_topic_owner(request, topic)
    
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个表单
        form = TopicForm()
    else:
        # POST提交数据：对数据进行处理
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
        
    # 显示空表单或指出表单数据无效
    context  = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)



@login_required
def new_entry(request, topic_id):
    """在特定主题中添加新条目"""
    topic = Topic.objects.get(id = topic_id)
    # 检查是否当前用户
    check_topic_owner(request, topic)
    
    if request.method != 'POST':
        # 未提交数据：创建一个空表单
        form = EntryForm()
    else:
        # POST 提交数据：对数据进行处理
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
    # 显示空表单或指出表单数据无效
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑既有的条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    # 验证用户
    check_topic_owner(request, topic)
    
    if request.method != 'POST':
    # 初次请求：使用当前的条目填充表单
        form = EntryForm(instance=entry)
    else:
    # POST 提交的数据：对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(request, topic):
    """验证用户"""
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404