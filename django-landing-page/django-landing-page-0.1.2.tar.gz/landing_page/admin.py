from django.contrib import admin
from .models import *


class ServicePartAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(ServicePart, ServicePartAdmin)


class TestimonialPartAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(TestimonialPart, TestimonialPartAdmin)


class PricingPartAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(PricingPart, PricingPartAdmin)


class PortfolioPartAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(PortfolioPart, PortfolioPartAdmin)


class LandingPageAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'slug', )
    search_fields = ('title', 'tagline',)
    exclude = ('user',)

    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(LandingPage, LandingPageAdmin)



class LayoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'folder_name')

admin.site.register(Layout, LayoutAdmin)
