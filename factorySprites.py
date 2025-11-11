import pygame
from mountain import Mountain
from cloud import Cloud

class FactorySprites:
    def __init__(self, prototypes, periods, base_event_type):
        assert len(prototypes) == len(periods)
        self._prototypes = prototypes
        self._periods = periods
        self._base = base_event_type

        # event_types serà una llista d'enters contigus començant per base
        self.event_types = [base_event_type + i for i in range(len(prototypes))]

        # Registrar timers a Pygame
        for i, ev in enumerate(self.event_types):
            pygame.time.set_timer(ev, self._periods[i])

    def make(self, event_type, group):
        """
        Crea un sprite a partir del seu event_type i assegura que,
        si és una Mountain, no col·lisiona amb sprites ja existents del grup.
        """
        try:
            idx = event_type - self._base
            prototype = self._prototypes[idx]
        except Exception as e:
            raise ValueError(
                f"event_type {event_type} no correspon a cap prototip de la fàbrica"
            ) from e

        # Crear primera instància
        sprite = prototype.clone()

        # ✅ Si és una muntanya → assegurar que no col·lisiona
        if isinstance(sprite, (Mountain, Cloud)):
            while pygame.sprite.spritecollide(sprite, group, dokill=False):
                sprite = prototype.clone()

        return sprite

