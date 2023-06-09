from django.urls import path
from . import views

urlpatterns = [
    path('listeleme/', views.listeleme, name='listeleme'),
    path('form/', views.form, name='form'),
    path('sss/', views.sss, name='sss'),
    path('sepet',views.sepet,name='sepet'),
    path('odeme', views.odeme, name='odeme'),
    path('Bossepet', views.Bossepet , name='Bossepet'),
    path('tamamlanma', views.tamamlanma , name='tamamlanma'),
    path('sil/<str:isim>/', views.sil , name='sil'),
    path('kartsil/<int:numara>/', views.kartsil , name='kartsil'),
    path('sepeti-temizle/', views.sepeti_temizle, name='sepeti_temizle'),
    path('bakiye_ekle/',views.bakiye_ekle,name="bakiye_ekle"),
    path('bakiyeden_al/',views.bakiyeden_al,name="bakiyeden_al"),
      path('login/', views.user_login_view, name='user_login_view'),
    path('logout/', views.logoutview, name='logoutview'),
    path('hesabim/', views.hesabim, name='hesabim'),
    path('kayitol/', views.kayitol, name='kayitol'),
    path('kayitol2/', views.register, name='register'),
    path('siparislerim/', views.siparislerim, name='siparislerim'),

    path('resetpassword/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='reset_password'),
    path('resetpassword_sent/', auth_views.PasswordResetDoneView.as_view(), name='reset_password_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetpassword_complete/', auth_views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),
]

