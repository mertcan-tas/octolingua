from rest_framework.pagination import CursorPagination

class AbstractCursorPagination(CursorPagination):
    page_size = 24 
    ordering = '-created_at'  
    cursor_query_param = 'searchAfter'