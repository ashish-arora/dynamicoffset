from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^Worldwide-Creations/$', 'printing.views.worldwide_creations'),
    url(r'^Brochures/$', 'printing.views.brochures'),
    url(r'^Business-Cards/$', 'printing.views.business_cards'),
    url(r'^Corporate-Stationery/$', 'printing.views.corporate_stationery'),
    url(r'^Envelopes/$', 'printing.views.envelopes'),
    url(r'^Folder-Covers/$', 'printing.views.folder_covers'),
    url(r'^LetterHeads/$', 'printing.views.letterheads'),
    url(r'^Banners/$', 'printing.views.banners'),
    url(r'^Calendars/$', 'printing.views.calendars'),
    url(r'^Catalogs-Booklets/$', 'printing.views.catalogs_booklets'),
    url(r'^Christmas-Cards/$', 'printing.views.christmas_cards'),
    url(r'^Flyers-Mailers/$', 'printing.views.flyers_mailers'),
    url(r'^Greeting-Cards/$', 'printing.views.greeting_cards'),
    url(r'^Marketing-Cards/$', 'printing.views.marketing_cards'),
    url(r'^Posters/$', 'printing.views.posters'),
    url(r'^Presentation-Folder-Wallets/$', 'printing.views.presentation_folder'),
    url(r'^Large-Quality-Merchandise/$', 'printing.views.large_quality_merchandise'),
    url(r'^Promotional-Merchandise/$', 'printing.views.promotional_merchandise'),
    url(r'^Canvas-Prints/$', 'printing.views.canvas_prints'),
    url(r'^Corporate-Calendars/$', 'printing.views.corporate_calendars'),
    url(r'^Cards-Stationery/$', 'printing.views.cards_stationery'),
    url(r'^Photo-Books/$', 'printing.views.photo_books'),
    url(r'^Folded_Brochures/$', 'printing.views.folded_brochures'),
    url(r'^Magzines_Booklets/$', 'printing.views.magzines_booklets'),
    url(r'^Graphic-Design/$', 'printing.views.graphic_design'),
    url(r'^Request-Quote/$', 'printing.views.request_quote'),
    url(r'^About/$', 'printing.views.about'),
    url(r'^Contact-Us/$', 'printing.views.contact_us'),
    url(r'^Request-Quote/$', 'printing.views.request_quote'),
    url(r'^home/$', 'printing.views.home'),
    url(r'^$', 'printing.views.home'),
    # Examples:
    # url(r'^$', 'offset.views.home', name='home'),
    # url(r'^offset/', include('offset.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
