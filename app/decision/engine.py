class DecisionDetails:
    name: str
    year: int
    profit_or_loss: dict[int, float]
    preassessment: float


class DecisionEngine:
    def request(details: DecisionDetails):
        return True
