from datetime import date, datetime, timezone, timedelta

#function views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

#classviews
from django.views.generic import DetailView, ListView
from django.db.models import Q

#custom models and forms
from .models import Articles
from .forms import SearchForm, DateForm

def day():
    delta=-5
    now = datetime.now(tz=timezone(timedelta(hours=delta)))
    return date(now.year, now.month, now.day)
    #return datetime(2020, 3, 17)

# Create your views here.
'''
@login_required
def articleListView(request):
    article_list=Articles.objects.filter(date = day())
    paginator=Paginator(article_list, 8)
    p_num=request.GET.get('page')
    page_obj=paginator.get_page(p_num)

    context={
        'articles':page_obj.object_list,
        'title':'All Stories',
        'topic':'All Stories',
        'form':SearchForm(),
        'page_obj':page_obj
    }

    return render(request, 'webapp_main/articles_list.html', context)
'''

def newsListView(request):
    article_list=Articles.objects.filter(tag__icontains="News", date=day())

    paginator=Paginator(article_list, 8)
    p_num=request.GET.get('page')
    page_obj=paginator.get_page(p_num)

    base=request.path.split('/')[1]
    if base == '':
        base='all'

    context={
        'articles':page_obj.object_list,
        'title':'Today\'s Stories',
        'topic':'News',
        'form':SearchForm(),
        'form_date': DateForm(),
        'page_obj':page_obj,

        'base': base
    }

    return render(request, 'webapp_main/articles_list.html', context)

@login_required
def archiveListView(request):
    if request.method == 'GET':
        article_list=Articles.objects.filter(date=request.GET["q"]).order_by('source')

        paginator=Paginator(article_list, 8)
        p_num=request.GET.get('page')
        page_obj=paginator.get_page(p_num)

        context={
            'articles':page_obj.object_list,
            'title': request.GET["q"]+' Stories',
            'topic':'News From '+request.GET["q"],
            #'form':SearchForm(),
            #'form_date': DateForm(),
            'q':request.GET["q"],
            'page_obj':page_obj,
            'base': request.GET['q']
        }

    return render(request, 'webapp_main/articles_list.html', context)

@login_required
def sportsListView(request, source, topic):
    if source == 'all':
        if topic != 'others':
            article_list=Articles.objects.filter(tag__icontains=topic, date=day())
        else:
            article_list=Articles.objects.exclude(Q(tag__icontains="News")|Q(tag="Sports")|Q(tag__icontains="Letters")).filter(date=day()).order_by('tag')

    elif source[:1].isdigit() and '-' in source:
        if topic != 'others':
            article_list=Articles.objects.filter(tag__icontains=topic, date=source)
        else:
            article_list=Articles.objects.exclude(Q(tag__icontains="News")|Q(tag="Sports")|Q(tag__icontains="Letters")).filter(date=source).order_by('tag')
    else:
        if topic != 'others':
            article_list=Articles.objects.filter(source__icontains=source, tag__icontains=topic, date=day())
        else:
            article_list=Articles.objects.exclude(Q(tag__icontains="News")|Q(tag="Sports")|Q(tag__icontains="Letters")).filter(source__icontains=source, date=day()).order_by('tag')

    paginator=Paginator(article_list, 8)
    p_num=request.GET.get('page')
    page_obj=paginator.get_page(p_num)

    context={
        'articles':page_obj.object_list,
        'title':source.upper(),
        'topic': source+' - '+topic,
        #'form':SearchForm(),
        'page_obj':page_obj,
        'base': source

    }

    return render(request, 'webapp_main/articles_list.html', context)

'''
@login_required
def lettersListView(request):
    article_list=Articles.objects.filter(tag__icontains="Letters", date=day())

    paginator=Paginator(article_list, 8)
    p_num=request.GET.get('page')
    page_obj=paginator.get_page(p_num)

    context={
        'articles':page_obj.object_list,
        'title':'Letters',
        'topic':'Letters',
        #'form':SearchForm(),
        'page_obj':page_obj
    }

    return render(request, 'webapp_main/articles_list.html', context)

@login_required
def othersListView(request):
    article_list=Articles.objects.exclude(Q(tag__icontains="News")|Q(tag="Sports")|Q(tag__icontains="Letters")).filter(date=day()).order_by('tag')

    paginator=Paginator(article_list, 8)
    p_num=request.GET.get('page')
    page_obj=paginator.get_page(p_num)

    context={
        'articles':page_obj.object_list,
        'title':'Others',
        'topic':'Everything Else',
        #'form':SearchForm(),
        'page_obj':page_obj
    }

    return render(request, 'webapp_main/articles_list.html', context)
'''

@login_required
def source(request, source):
    article_list=Articles.objects.filter(source__icontains=source, date=day())
    paginator=Paginator(article_list, 8)
    p_num=request.GET.get('page')
    page_obj=paginator.get_page(p_num)

    context={
        'articles':page_obj.object_list,
        'title':source.upper(),
        'topic':source+' news',
        #'form':SearchForm(),
        'page_obj':page_obj,
        'base': source
    }

    return render(request, 'webapp_main/articles_list.html', context)

'''
@login_required
def source01_ListView(request):
    article_list=Articles.objects.filter(source__icontains="kaieteur", date=day())
    paginator=Paginator(article_list, 8)
    p_num=request.GET.get('page')
    page_obj=paginator.get_page(p_num)

    context={
        'articles':page_obj.object_list,
        'title':'Kaieteur',
        'topic':'kaieteur news',
        #'form':SearchForm(),
        'page_obj':page_obj
    }

    return render(request, 'webapp_main/articles_list.html', context)

@login_required
def source02_ListView(request):
    article_list=Articles.objects.filter(source__icontains="stabroek", date=day())
    paginator=Paginator(article_list, 8)
    p_num=request.GET.get('page')
    page_obj=paginator.get_page(p_num)

    context={
        'articles':page_obj.object_list,
        'title':'Stabroek',
        'topic':'stabroek news',
        #'form':SearchForm(),
        'page_obj':page_obj
    }

    return render(request, 'webapp_main/articles_list.html', context)
'''

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model=Articles
    context_object_name='article'

    query_pk_and_slug = True
    
'''
class SearchView(LoginRequiredMixin, ListView):
    model=Articles

    context_object_name='articles'
    paginate_by=8

    def get_queryset(self):
        query=self.request.GET.get('q')

        return Articles.objects.filter(title__icontains=query).order_by('source')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        if self.request.GET.get('q'):
            context['q']=self.request.GET.get('q')
            #print(context['q'])
        context['base']='all'
        return context
'''

@login_required
def SearchView(request):
    if request.method == 'GET':
        article_list=Articles.objects.filter(title__icontains=request.GET["q"]).order_by('source')

        paginator=Paginator(article_list, 8)
        p_num=request.GET.get('page')
        page_obj=paginator.get_page(p_num)

        context={
            'articles':page_obj.object_list,
            'title': request.GET["q"]+' Results',
            'topic':'Results For "'+request.GET["q"]+'"',
            #'form':SearchForm(),
            #'form_date': DateForm(),
            'q':request.GET["q"],
            'page_obj':page_obj,
            'base': 'search/'+request.GET["q"]
        }

    return render(request, 'webapp_main/articles_list.html', context)

@login_required
def SearchView_Filter(request, query, topic):
    if request.method == 'GET':
        if topic != 'others':
            article_list=Articles.objects.filter(tag__icontains=topic, title__icontains=query)
        else:
            article_list=Articles.objects.exclude(Q(tag__icontains="News")|Q(tag="Sports")|Q(tag__icontains="Letters")).filter(tag__icontains=topic, title__icontains=query).order_by('tag')

        paginator=Paginator(article_list, 8)
        p_num=request.GET.get('page')
        page_obj=paginator.get_page(p_num)

        context={
            'articles':page_obj.object_list,
            'title': query+' Results',
            'topic':'Results For "'+query+'"',
            #'form':SearchForm(),
            #'form_date': DateForm(),
            'q':query,
            'page_obj':page_obj,
            'base': 'search/'+query
        }

    return render(request, 'webapp_main/articles_list.html', context)