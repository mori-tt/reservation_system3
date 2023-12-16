from django.urls import path
from app import views

urlpatterns = [
    path('', views.StoreView.as_view(), name="store"),
    path('store/<int:pk>/', views.StaffView.as_view(), name='staff'), # 追加
    path('calendar/<int:pk>/', views.CalendarView.as_view(), name='calendar'), # 追加
    path('calendar/<int:pk>/<int:year>/<int:month>/<int:day>/', views.CalendarView.as_view(), name='calendar'), # 追加
    path('booking/<int:pk>/<int:year>/<int:month>/<int:day>/<int:hour>/', views.BookingView.as_view(), name='booking'), # 追加
    path('thanks/', views.ThanksView.as_view(), name='thanks'), # 追加
    path('mypage/<int:year>/<int:month>/<int:day>/', views.MyPageView.as_view(), name='mypage'), # 追加
    path('mypage/holiday/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Holiday, name='holiday'), # 追加
    path('mypage/delete/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Delete, name='delete'), # 追加
]