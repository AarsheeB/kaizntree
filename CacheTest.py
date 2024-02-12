from django.core.cache import cache

cache_key = 'item_list'
cache.delete(cache_key)
