from django.contrib import admin
import admin_thumbnails

from .models import *
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    list_display = ['id']
    model = Images
    readonly_fields = ('id',)
    extra = 1


@admin_thumbnails.thumbnail('image')
class ProjectImageInline(admin.TabularInline):
    list_display = ['id']
    model = Project_Images
    readonly_fields = ('id',)
    extra = 1


@admin_thumbnails.thumbnail('image')
class ServiceImageInline(admin.TabularInline):
    list_display = ['id']
    model = Service_Images
    readonly_fields = ('id',)
    extra = 1



class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag','featured_project', 'Top_Deals_Of_The_Day','Top_Selling_Products','Recommended_For_You', 'slug', 'create_at','update_at',]
    list_editable = ['featured_project', 'Top_Deals_Of_The_Day','Top_Selling_Products','Recommended_For_You']
    inlines = [ProductImageInline,]

admin.site.register(Product,ProductAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag', 'Project_Type','featured_project',  'slug', 'create_at','update_at',]
    list_editable = ['featured_project','Project_Type',]
    inlines = [ProjectImageInline,]

admin.site.register(Project,ProjectAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag','featured_project',  'slug', 'create_at','update_at',]
    list_editable = ['featured_project',]
    inlines = [ServiceImageInline,]

admin.site.register(Service,ServiceAdmin)

admin.site.register(Images)
admin.site.register(Project_Images)
admin.site.register(Service_Images)
admin.site.register(Comment)



