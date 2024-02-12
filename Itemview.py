from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'tags', 'quantity', 'price', 'supplier', 'stock_status']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
         # Check if the data is already in the cache
        cache_key = 'item_list'
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data

        # If not in cache, fetch data from the database
        queryset = Item.objects.all()

        # Example: Filtering based on date range (modify as needed)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            queryset = queryset.filter(transaction_date__range=(start_date, end_date))

          # Store the data in the cache for future requests
        cache.set(cache_key, queryset)


        return queryset

class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer






   
       

        # Store the data in the cache for future requests
        cache.set(cache_key, queryset)

        return queryset








