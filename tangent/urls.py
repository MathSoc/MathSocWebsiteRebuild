from django.conf.urls import patterns, include, url

urlpatterns = patterns('tangent.views',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home', name='tangent_home'),
    url(r'^log/', 'log', name='tangent_log'),
    url(r'^profile/', 'profile', name='tangent_profile'),
    url(r'^HELP$', 'help', name='tangent_help'),
    url(r'^website/', 'website', name='tangent_website'),
    url(r'^(?P<org_id>\d+)/', 'organization', name='tangent_organization')
)
