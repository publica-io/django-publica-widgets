from django.conf import settings


MAP_POI_CATEGORIES = getattr(
    settings, 'WIDGETS_MAP_POI_CATEGORIES', (
    	('food', 'Food'),
    	('places', 'Places to see'),
    	('Bars', 'Bars to drink'),
    )
)
