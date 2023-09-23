from django.db import models


class AdultSizing:
    class ClothingSize(models.TextChoices):
        EXTRA_SMALL = 'XS', 'Extra small'
        SMALL = 'S', 'Small'
        MEDIUM = 'M', 'Medium'
        LARGE = 'L', 'Large'
        EXTRA_LARGE = 'XL', 'Extra large'
        EXTRA_EXTRA_LARGE = 'XXL', 'Extra extra large'

    class ShoeSize(models.TextChoices):
        THIRTY_EIGHT = '38'
        THIRTY_NINE = '39'
        FORTY = '40'
        FORTY_HALF = '40.5'
        FORTY_ONE = '41'
        FORTY_ONE_HALF = '41.5'
        FORTY_TWO = '42'
        FORTY_TWO_HALF = '42.5'
        FORTY_THREE = '43'
        FORTY_THREE_HALF = '43.5'
        FORTY_FOUR = '44'
        FORTY_FIVE = '45'
        FORTY_SIX = '46'
