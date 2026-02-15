from django.contrib import admin 
from .models import Member 
@admin.register(Member) 
class MemberAdmin(admin.ModelAdmin): 
 list_display = ['member_id', 'user', 'phone_number', 'is_active',   'membership_date'] 
 list_filter = ['is_active', 'membership_date'] 
 search_fields = ['member_id', 'user__username', 'user__first_name',   'user__last_name', 'phone_number'] 
 readonly_fields = ['membership_date']
