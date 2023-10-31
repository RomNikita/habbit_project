from rest_framework.pagination import PageNumberPagination


class UserHabbitsPaginator(PageNumberPagination):
    page_size = 5
