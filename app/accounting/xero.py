from app.accounting.details import Details
from app.accounting.provider import Provider


class ProviderXero(Provider):
    def get_balance_sheet(self, details: Details):
        return \
        [
            {
                "year": 2020,
                "month": 12,
                "profit": 250000,
                "assetsValue": 1234
            },
            {
                "year": 2020,
                "month": 11,
                "profit": 1150,
                "assetsValue": 5789
            },
            {
                "year": 2020,
                "month": 10,
                "profit": 2500,
                "assetsValue": 22345
            },
            {
                "year": 2020,
                "month": 9,
                "profit": -187000,
                "assetsValue": 223452
            }
        ]
