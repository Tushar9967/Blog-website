from django.conf.urls import url
from blogapp import views
from django.urls import path
app_name = 'blogapp'

urlpatterns = [url('about/', views.about, name='about'),
               url('register/', views.register, name='register'),
               url('user_login/', views.user_login, name='user_login'),
               url('newpost/', views.NewPostView, name='newpost'),
               url('drafts/', views.DraftsView.as_view(), name='drafts'),
               path('<int:pk>', views.DraftsEditView.as_view(), name='view_draft'),
               path('update/<int:pk>/',
                    views.DraftsUpdateView.as_view(), name='update'),
               path('delete/<int:pk>/',
                    views.DraftsDeleteView.as_view(), name='delete'),
               path('post/publish/<int:pk>/',
                    views.post_publish, name='post_publish'),
               path('post/comment/<int:pk>/', views.CommentView, name='comment'),
               path('comment/<int:pk>/approve/',
                    views.comment_approve, name='comment_approve'),
               path('comment/<int:pk>/remove/',
                    views.comment_remove, name='comment_remove'),
               path('getstarted/', views.started, name='started'),

               # path('<id>/delete',views.DraftsDeleteView,name='delete')
               ]
#
