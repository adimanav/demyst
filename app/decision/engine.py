from typing import Dict


class DecisionDetails:
    name: str
    year: int
    profit: Dict[int, float]
    preassessment: float


class DecisionEngine:
    def request(self, details: DecisionDetails):
        return True
