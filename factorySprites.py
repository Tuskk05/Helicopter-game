import pygame

class FactorySprites:
    """
    Gestiona un llistat de prototips i períodes (en ms).
    - prototypes: llista d'instàncies que implementen .clone()
    - periods: llista d'enters (ms) amb la mateixa longitud
    - base_event_type: primer event type (p.ex. pygame.USEREVENT + 1)
    La classe crea timers per a cada prototype/event i ofereix make(event_type)
    """
    def __init__(self, prototypes, periods, base_event_type):
        assert len(prototypes) == len(periods), "prototypes i periods han de tenir la mateixa longitud"
        self._prototypes = prototypes
        self._periods = periods
        self._base = base_event_type
        # event_types serà una llista d'enters contigus començant per base
        self.event_types = [base_event_type + i for i in range(len(prototypes))]
        # Registrar timers a Pygame
        for i, ev in enumerate(self.event_types):
            pygame.time.set_timer(ev, self._periods[i])

    def make(self, event_type):
        """Clona i retorna una nova instància segons l'event_type rebut."""
        try:
            idx = event_type - self._base
            prototype = self._prototypes[idx]
        except Exception as e:
            raise ValueError(f"event_type {event_type} no correspon a cap prototip de la fàbrica") from e
        return prototype.clone()
