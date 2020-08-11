from strategy.strategies.StrategyInterface import StrategyInterface


class AdditionStrategy(StrategyInterface):
    def execute(self, num1: int, num2: int) -> int:
        return num1 + num2
