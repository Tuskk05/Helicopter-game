import pygame
from mountain import Mountain
from cloud import Cloud

class FactorySprites:
    def __init__(self, prototypes, periods, base_event_type):
        assert len(prototypes) == len(periods)
        self._prototypes = prototypes
        self._periods = periods
        self._base = base_event_type

        self.event_types = [base_event_type + i for i in range(len(prototypes))]

        for i, ev in enumerate(self.event_types):
            pygame.time.set_timer(ev, self._periods[i])

    def make(self, event_type, group):
        try:
            idx = event_type - self._base
            prototype = self._prototypes[idx]
        except Exception as e:
            raise ValueError(
                f"event_type {event_type} no correspon a cap prototip de la fàbrica"
            ) from e

        sprite = prototype.clone()

        if isinstance(sprite, (Mountain, Cloud)):
            while pygame.sprite.spritecollide(sprite, group, dokill=False):
                sprite = prototype.clone()

        return sprite

