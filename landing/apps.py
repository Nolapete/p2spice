from django.apps import AppConfig


class LandingConfig(AppConfig):
    name = "landing"
    verbose_name = "P2's Spice Landing"

    def ready(self):
        from django.contrib import admin

        admin.site.site_header = "p2spice.com Administration"
        admin.site.site_title = "p2spice.com"
        admin.site.index_title = "P2's Spice Company Admin Portal"
