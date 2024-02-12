# inventory_project/settings.py

INSTALLED_APPS = [
    # other apps
    'drf_yasg',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # other context processors
                'django.template.context_processors.request',
            ],
        },
    },
]
