from django.contrib import admin

from .models import Post, Category, Tag, Feedback


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    filter_horizontal = ('tags',)


class CategoryAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class FeedbackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Feedback, FeedbackAdmin)
