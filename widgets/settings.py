from django.conf import settings


MAP_POI_KINDS = getattr(
    settings, 'WIDGETS_MAP_POI_CATEGORIES', (
        ('place-see', 'Place to See'),
        ('plase-eat', 'Place to Eat')
    )
)

MAP_POI_CATEGORIES = getattr(
    settings, 'WIDGETS_MAP_POI_KINDS', (
        ('cafe', 'Coffee'),
        ('bar', 'Bar'),
        ('food', 'Food')
    )
)
