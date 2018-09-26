"""
Custom fuzzy attribute for MediaItem code to be used with FactoryBoy
"""
import random
import string
from factory.fuzzy import BaseFuzzyAttribute


class FuzzyMediaItemCode(BaseFuzzyAttribute):
    """
    MediaItem code fuzzy attribute
    """

    def fuzz(self):
        """
        Return value
        """

        return '{}_{}_{}_{}_{}'.format(
            ''.join(random.choice(string.ascii_uppercase) for _ in range(4)),
            ''.join(random.choice(string.ascii_uppercase) for _ in range(3)),
            ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)),
            random.randint(1000, 9999),
            random.randint(100, 999)
        )
