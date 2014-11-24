from django.conf import settings


MAP_POI_ACTIVITIES = getattr(
    settings, 'WIDGETS_MAP_POI_ACTIVITIES', (
        ('place-see', 'Place to See'),
        ('plase-eat', 'Place to Eat')
    )
)

MAP_POI_CATEGORIES = getattr(
    settings, 'WIDGETS_MAP_POI_CATEGORIES', (
        ('bar', 'Bar'),
        ('cafe', 'Coffee'),
        ('food', 'Food')
    )
)
