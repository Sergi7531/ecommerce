from django.db import models


class KidSizing:
    class ClothingSize(models.TextChoices):
        FOUR_FIVE = '110cm'
        SIX_SEVEN = '122cm'
        EIGHT_NINE = '134cm'
        TEN_ELEVEN = '146cm'
        TWELVE_FOURTEEN = '164cm'

    class ShoeSize(models.TextChoices):
        THIRTY_TWO = '32'
        THIRTY_THREE = '33'
        THIRTY_FOUR = '34'
        THIRTY_FIVE = '35'
        THIRTY_SIX = '36'
        THIRTY_SEVEN = '37'
        THIRTY_EIGHT = '38'
        THIRTY_NINE = '39'
        FORTY = '40'

