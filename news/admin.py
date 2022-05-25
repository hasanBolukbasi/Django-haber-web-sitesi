from django.contrib import admin


from news.models import Category, Comment, News, Images, Faq, Message


class NewsImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['rate', 'status']
    list_filter = ['status']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)
    inlines = [NewsImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']
    list_filter = ['question']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['email', 'message']
    list_filter = ['message']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Message, MessageAdmin)



