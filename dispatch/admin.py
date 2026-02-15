from django.contrib import admin 
from .models import BorrowRecord 
@admin.register(BorrowRecord) 
class BorrowRecordAdmin(admin.ModelAdmin): 
 list_display = ['book', 'member', 'borrow_date', 'due_date',   'return_date', 'status'] 
 list_filter = ['status', 'borrow_date', 'due_date']  
 search_fields = ['book__title', 'member__member_id',   'member__user__username'] 
 readonly_fields = ['borrow_date'] 
  
 def get_queryset(self, request): 
  qs = super().get_queryset(request) 
  return qs.select_related('book', 'member', 'member__user')
