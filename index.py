from strategy.StrategyInterface import StrategyInterface
from strategy.AdditionStrategy import AdditionStrategy


class Calculator(object):
    def __init__(self, strategy: StrategyInterface):
        self.strategy = strategy

    def compute(self, num1: int, num2: int) -> int:
        return self.strategy.execute(num1, num2)


addition_strategy = AdditionStrategy()
calc = Calculator(addition_strategy)
print(calc.compute(1, 2))
