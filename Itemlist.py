from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        # Filter based on query parameters
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        stock_status = self.request.query_params.get('stock_status', None)

        if start_date and end_date:
            queryset = queryset.filter(created_at__range=[start_date, end_date])

        if stock_status:
            if stock_status == 'available':
                queryset = queryset.filter(quantity__gt=0)
            elif stock_status == 'out_of_stock':
                queryset = queryset.filter(quantity=0)

        return queryset
