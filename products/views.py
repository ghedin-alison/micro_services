from rest_framework import viewsets


class ProductViewSet(viewsets.ViewSet):
    def list_products(self, request):  # get /api/products
        pass

    def create_product(self, request):  # post /api/products
        pass

    def retrieve_product(self, request, pk=None):  # get /api/products/<str:id>
        pass

    def update_product(self, request, pk=None):  # update /api/products/<str:id>
        pass

    def destroy_product(self, request, pk=None):  # delete /api/products/<str:id>
        pass