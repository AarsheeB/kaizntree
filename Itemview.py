from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Item
from .serializers import ItemSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'tags', 'quantity', 'price', 'supplier', 'stock_status']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Item.objects.all()

        # Example: Filtering based on date range (modify as needed)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            queryset = queryset.filter(transaction_date__range=(start_date, end_date))

        return queryset

class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer










