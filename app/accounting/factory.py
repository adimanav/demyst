from app.accounting.xero import ProviderXero
from app.accounting.myob import ProviderMyob


class ProviderFactory:
    def get_provider(self, name: str):
        if name == "xero":
            return ProviderXero()
        elif name == "myob":
            return ProviderMyob()
