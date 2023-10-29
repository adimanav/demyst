from abc import ABC, abstractmethod
from details import Details

class Provider(ABC):
    @abstractmethod
    def get_balance_sheet(self, details: Details):
        pass
