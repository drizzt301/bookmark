from django.urls import path
from .views import *

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),  # 클래스 형 뷰 일경우에는 뒤에 .as_view()를 사용해야 정상 동작
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),  # int 타입 - 0을 포함한 양의 정수와 매칭
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]