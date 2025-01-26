import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from .models import *



class Follow_UpInline(admin.TabularInline):
    model = Follow_Up
    extra = 1
    show_change_link = True

class MeetingInline(admin.TabularInline):
    model = Meeting
    extra = 1
    show_change_link = True


class ResponseAdmin(admin.ModelAdmin):
    list_display = ['id','name','contact_no', 'call_comment','description','meeting_follow_up', 'response_status', 'city','locality','email_id','create_at','update_at','response_from',]    
    
    list_filter = ['meeting_follow_up','response_status','response_from','city','locality',]
    search_fields = ['name','email_id','contact_no', 'description',]
    list_editable = ['response_status', 'meeting_follow_up', 'call_comment','city','locality',]
    list_per_page = 10
    inlines = [Follow_UpInline,MeetingInline]

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['id','meeting','comment', 'name','locality','city','create_at','update_at',]    
    
    list_filter = ('meeting','create_at','update_at','city','locality',) 
    list_editable = ['meeting', 'comment']

    list_per_page = 30


class Follow_UpAdmin(admin.ModelAdmin):
    list_display = ['id','follow_up','comment','name','locality','city', 'create_at','update_at']    
    
    list_filter = ('follow_up','create_at','update_at','city','locality',) 
    list_editable = ['follow_up', 'comment']

    list_per_page = 30 




admin.site.register(Follow_Up,Follow_UpAdmin)
admin.site.register(Meeting,MeetingAdmin)
admin.site.register(Response,ResponseAdmin)
admin.site.register(Response_From,)
admin.site.register(Response_Status,)








