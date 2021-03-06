# cltlanglab/urls-dev.py urls for use in local development. key diff is a different login url is used (not cas).

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

from core.views import IndexView, HomeView, CourseListView, CourseIndexView, CourseCreateView, CourseUpdateView, CourseDeleteView, CourseCopyView, ActivityCreateIndexView, LessonUpdateView, LessonCreateView, LessonAddView, PostDeleteView, PostSaveView, fileUpload, subscribeCourse, changePerm, copyActivity, editLessonTitle, editEssayDraft, uhcaslogout
from discussions.views import DiscussionCreateView, DiscussionDetailView, DiscussionUpdateView, DiscussionDeleteView
from essays.views import EssayCreateView, EssayDetailView, EssayUpdateView, EssayDeleteView, EssayResponseUpdateView
from overdub_discussions.views import OverdubCreateView, OverdubDetailView, OverdubUpdateView, OverdubDeleteView
from flatpage.views import FlatpageDetailView, FlatpageCreateView, FlatpageUpdateView, FlatpageDeleteView
from settings import base
from flatpage.views import FlatpageDetailView, FlatpageCreateView, FlatpageUpdateView, FlatpageDeleteView, deleteAttachment
#import django_cas_ng
#import socketio.sdjango
#socketio.sdjango.autodiscover()

urlpatterns = patterns('',
    url(r'^course/(?P<pk>\d+)$', CourseIndexView.as_view(), name='course'),
    url(r'^course/add/$', CourseCreateView.as_view(), name='create_collection'),
    url(r'^course/edit/(?P<pk>\d+)$', CourseUpdateView.as_view(), name='edit_collection'),
    url(r'^course/delete/(?P<pk>\d+)$', CourseDeleteView.as_view(), name='delete_collection'),
    url(r'^course/copy/(\w+)/$', CourseCopyView, name='copy_collection'),
    url(r'^lesson/edit/(?P<pk>\d+)$', LessonUpdateView.as_view(), name='edit_lesson'),
    url(r'^lesson/add/(?P<addpk>\d+)$', LessonCreateView.as_view(), name='create_lesson'),
    url(r'^lesson/add2/(?P<addpk>\d+)$', LessonAddView.as_view(), name='add_lesson'),
    url(r'^activity/add/(?P<pk>\d+)$', ActivityCreateIndexView.as_view(), name='create_activity'),
    url(r'^discussion/(?P<pk>\d+)$', DiscussionDetailView.as_view(), name='discussion'),
    url(r'^discussion/add/(?P<pk>\d+)$', DiscussionCreateView.as_view(), name='create_discussion'),
    url(r'^discussion/edit/(?P<pk>\d+)$', DiscussionUpdateView.as_view(), name='edit_discussion'),
    url(r'^discussion/delete/(?P<pk>\d+)$', DiscussionDeleteView.as_view(), name='delete_discussion'),
    url(r'^essay/(?P<pk>\d+)$', EssayDetailView.as_view(), name='essay'),
    url(r'^essay/add/(?P<pk>\d+)$', EssayCreateView.as_view(), name='create_essay'),
    url(r'^essay/edit/(?P<pk>\d+)$', EssayUpdateView.as_view(), name='edit_essay'),
    url(r'^essay/delete/(?P<pk>\d+)$', EssayDeleteView.as_view(), name='delete_essay'),
    url(r'^essay/grade/(?P<pk>\d+)$', EssayResponseUpdateView.as_view(), name='grade_essay'),
    url(r'^flatpage/(?P<pk>\d+)$', FlatpageDetailView.as_view(), name='flatpage'),
    url(r'^flatpage/add/(?P<pk>\d+)$', FlatpageCreateView.as_view(), name='create_flatpage'),
    url(r'^flatpage/edit/(?P<pk>\d+)$', FlatpageUpdateView.as_view(), name='edit_flatpage'),
    url(r'^flatpage/delete/(?P<pk>\d+)$', FlatpageDeleteView.as_view(), name='delete_flatpage'),
    url(r'^attachment/delete/$', deleteAttachment, name='delete_attachment'),
    url(r'^overdub/(?P<pk>\d+)$', OverdubDetailView.as_view(), name='overdub'),
    url(r'^overdub/add/(?P<pk>\d+)$', OverdubCreateView.as_view(), name='create_overdub'),
    url(r'^overdub/edit/(?P<pk>\d+)$', OverdubUpdateView.as_view(), name='edit_overdub'),
    url(r'^overdub/delete/(?P<pk>\d+)$', OverdubDeleteView.as_view(), name='delete_overdub'),
    url(r'^searchcourse/$', CourseListView.as_view(), name='course_list'),
    url(r'^post/save/$',PostSaveView.as_view(), name='save_post'),
    url(r'^post/delete/$', PostDeleteView.as_view(), name='delete_post'),
    url(r'^upload/$', fileUpload, name='file_upload'),
    url(r'^subscribe/(\w+)/$', subscribeCourse, name='subscribe_course'),
    url(r'^perm/change/$', changePerm, name='change_perm'),
    url(r'^activity/copy/$', copyActivity, name='copy_activity'),
    url(r'^lesson/title/edit/$', editLessonTitle, name='edit_lesson_title'),
    url(r'^essaydraft/edit/$', editEssayDraft, name='edit_essay_draft'),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^socket\.io', include(socketio.sdjango.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
#
    # url(r'^accounts/login/$', 'django_cas.views.login', name='login'),
    # url(r'^accounts/logout/$', uhcaslogout, name='logout'),

    # url(r'^accounts/login/$', 'django_cas_ng.views.login', name='login'),
    # url(r'^accounts/logout/$', uhcaslogout, name='logout'),
    # url(r'^accounts/callback$', 'django_cas_ng.views.callback', name='cas_ng_proxy_callback'),

    url(r'^crossdomain.xml$','flashpolicies.views.simple',{'domains': ['*']}),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^$', IndexView.as_view(), name='landing'),
    url(r'^profile/', include('user_profile.urls', namespace='profile')),

)
urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)
