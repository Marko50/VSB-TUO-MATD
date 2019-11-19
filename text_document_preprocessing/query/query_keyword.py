from enum import Enum


class QueryKeyword(Enum):
    AND = 0
    OR = 1
    NOT = 2

    def key(self):
        return self.name

    def count(self):
        return len(self.key())
