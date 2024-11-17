from django.contrib import admin


class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'user_tg_id', 'name', 'age', 'location', 'is_military', 
        'educational_goal', 'telephone', 'is_end', 
        'is_completed', 'created_at', 'updated_at', 'deleted_at'
    )
    list_filter = ('is_military', 'is_end', 'is_completed', 'created_at', 'deleted_at')
    search_fields = ('user_tg_id__username', 'name', 'telephone', 'educational_goal')
    list_editable = ('is_end', 'is_completed')
    fields = (
        'user_tg_id', 'name', 'age', 'location', 'is_military', 
        'educational_goal', 'telephone', 'is_end', 
        'is_completed', 'completion_comment', 'created_at', 'updated_at', 'deleted_at'
    )
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
