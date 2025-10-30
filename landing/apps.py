from django.apps import AppConfig


class LandingConfig(AppConfig):
    name = "landing"
    verbose_name = "P2's Spice Landing"

    def ready(self):
        from django.contrib import admin

        admin.site.site_header = "config.com Administration"
        admin.site.site_title = "config.com"
        admin.site.index_title = "P2's Spice Company Admin Portal"
