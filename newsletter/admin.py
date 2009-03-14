from django.contrib import admin
from models import Subscription, NewsletterGroup

class SubscriptionAdmin(admin.ModelAdmin):
    
    list_display = ('email', 'name', 'subscribed', 'created_on', )
    search_fields = ('email',)
    list_filter = ('newsletter_groups', 'created_on', 'subscribed', )
    
    
class NewsletterGroupAdmin(admin.ModelAdmin):
    pass
        
    
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(NewsletterGroup, NewsletterGroupAdmin)
