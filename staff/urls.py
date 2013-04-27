from django.conf.urls import patterns, url
from django.conf import settings
from views import NewUser, UpdateUser

urlpatterns = patterns('staff.views',
    # Views in views.py
    url(r'^$', 'home'),
    url(r'^userdetail/(?P<uid>\d+)/$', 'userdetail'),
    url(r'^groupdetail/(?P<gid>\d+)/$', 'groupdetail'),
    url(r'^audit-by-cred/(?P<cred_id>\d+)/$', 'audit_by_cred'),
    url(r'^audit-by-user/(?P<user_id>\d+)/$', 'audit_by_user'),
    url(r'^audit-by-days/(?P<days_ago>\d+)/$', 'audit_by_days'),
    url(r'^change-advice-by-user/(?P<user_id>\d+)/$', 'change_advice_by_user'),
    url(r'^change-advice-by-user-and-group/(?P<user_id>\d+)/(?P<group_id>\d+)/$', 'change_advice_by_user_and_group'),
    url(r'^keepass-import/$', 'import_from_keepass'),
    url(r'^credundelete/(?P<cred_id>\d+)/$', 'credundelete'),
)

# URLs that we don't want with LDAP
if not settings.LDAP_ENABLED:
    urlpatterns += patterns('staff.views',
        url(r'^groupadd/$', 'groupadd'),
        url(r'^groupedit/(?P<gid>\d+)/$', 'groupedit'),
        url(r'^groupdelete/(?P<gid>\d+)/$', 'groupdelete'),
        url(r'^useradd/$', NewUser.as_view(), name="user_add"),
        url(r'^useredit/(?P<pk>\d+)/$', UpdateUser.as_view(), name="user_edit"),
        url(r'^userdelete/(?P<uid>\d+)/$', 'userdelete'),
    )
