from xero import ProviderXero
from myob import ProviderMyob


class ProviderFactory:
    def get_provider(self, name: str):
        if name == "xero":
            return ProviderXero()
        elif name == "myob":
            return ProviderMyob()
