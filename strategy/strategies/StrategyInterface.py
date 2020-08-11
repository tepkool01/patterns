from abc import abstractmethod


class StrategyInterface(object):
    @abstractmethod
    def execute(self, num1: int, num2: int):
        pass