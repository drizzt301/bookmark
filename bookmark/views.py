from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6


class BookmarkCreateView(CreateView):
    model = Bookmark                    # model 변수를 Bookmark 로 설정
    fields = ['site_name', 'url']       # 어떤 필드를 입력받을지 선택
    success_url = reverse_lazy('list')  # 목록페이지로 이동 success_url 사용방법 확인
    template_name_suffix = '_create'    # 모델명_xxx, 접미사 _form => _create --.html 파일 이름이 bookmark_create 된다


class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
