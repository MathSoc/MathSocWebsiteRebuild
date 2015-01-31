from django.conf.urls import patterns, include, url

urlpatterns = patterns('tangent.views',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home', name='tangent_home'),

)
