from django.contrib import admin
from board.models import Entry, Category, Board, FlatPage


class AdminBoard(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'items_per_page', 'is_admin')
    list_display_links = ('id',)
    list_editable = ('title', 'name', 'items_per_page', 'is_admin')
    search_fields = ['title', 'name', ]
    ordering = ('title',)


class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'board', 'title', 'name',)
    list_display_links = ('id',)
    list_editable = ('title', 'name', 'board',)
    list_filter = ('board',)
    search_fields = ['title', 'name', 'board', ]
    ordering = ('board', 'title', 'id',)


class AdminEntry(admin.ModelAdmin):
    list_display = ('id', 'board', 'category', 'parent', 'title', 'user', 'ip')
    list_display_links = ('id',)
    list_filter = ('board', 'category',)
    list_per_page = 20
    raw_id_fields = ('user',)
    date_hierarchy = 'created_date'
    save_on_top = True
    save_as = True
    ordering = ('-id',)
    search_fields = ('title', 'contents',)


class Admin_FlatPage(admin.ModelAdmin):
    list_display = ('id', 'entry', 'name')
    list_filter = ('entry',)
    list_per_page = 20
    raw_id_fields = ('entry',)
    save_on_top = True
    save_as = True
    search_fields = ('entry', 'name',)


admin.site.register(Category, AdminCategory)
admin.site.register(Board, AdminBoard)
admin.site.register(Entry, AdminEntry)
admin.site.register(FlatPage, Admin_FlatPage)
