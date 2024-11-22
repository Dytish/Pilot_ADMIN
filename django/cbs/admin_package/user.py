from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_tg_id', 'username', 'first_name', 
        'last_name', 'language_code', 'is_bot', 
        'is_active', 'created_at', 'updated_at', 'deleted_at'
    )
    list_filter = ('is_bot', 'is_active', 'language_code', 'created_at', 'deleted_at')
    search_fields = ('user_tg_id', 'username', 'first_name', 'last_name')
    list_editable = ('is_active',)
    fields = (
        'user_tg_id', 'username', 'first_name', 
        'last_name', 'language_code', 'is_bot', 
        'is_active', 'created_at', 'updated_at', 'deleted_at'
    )
    readonly_fields = ('created_at', 'updated_at')

    ordering = ('-created_at',)