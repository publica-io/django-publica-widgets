from django.conf import settings


MAP_POI_ACTIVITIES = getattr(
    settings, 'WIDGETS_MAP_POI_ACTIVITIES', (
        ('place-see', 'Place to See'),
        ('place-eat', 'Place to Eat')
    )
)

MAP_POI_VENUES = getattr(
    settings, 'WIDGETS_MAP_POI_VENUES', (
        ('atm', 'ATM'),
        ('bar', 'Bar'),
        ('cafe', 'Coffee'),
        ('food', 'Food'),
        ('landmark', 'Landmark'),
        ('library', 'Library'),
        ('pin', 'Red Centre'),
        ('shops', 'Shops'),
        ('wifi', 'Wi-Fi'),
        ('wildlife', 'Wildlife')
    )
)
