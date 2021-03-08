from rest_framework.pagination import PageNumberPagination


class PaginationPerTen(PageNumberPagination):
    page_size = 10
