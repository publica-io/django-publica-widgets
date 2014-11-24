from django.conf import settings


MAP_POI_ACTIVITIES = getattr(
    settings, 'WIDGETS_MAP_POI_ACTIVITIES', (
        ('place-see', 'Place to See'),
        ('plase-eat', 'Place to Eat')
    )
)

MAP_POI_VENUES = getattr(
    settings, 'WIDGETS_MAP_POI_VENUES', (
        ('bar', 'Bar'),
        ('cafe', 'Coffee'),
        ('food', 'Food')
    )
)
