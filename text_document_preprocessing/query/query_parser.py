from .node import Node
from .query_keyword import QueryKeyword


class QueryParser(object):

    def __init__(self, query):
        self._query = query
        self._query_count = len(self._query)

    def parse(self):
        self._eat_whitespaces()
        tree = self._expression()
        self._eat_whitespaces()
        if self._has_next():
            raise Exception("Wrong syntax! at (" + str(self._query_count - len(self._query)) + ")")
        return tree

    # General methods

    def _has_next(self, count=0):
        return len(self._query) > count

    def _peek(self, count=1):
        return self._query[:count]

    def _eat(self, symbol, count=1):
        if self._peek(count=count) == symbol:
            self._query = self._query[count:]
        else:
            raise Exception("Wrong syntax! at (" + str(self._query_count - len(self._query)) + ")")

    def _eat_whitespaces(self):
        while self._has_next():
            if self._peek() == " ":
                self._eat(self._peek())
            else:
                break

    def _next(self):
        symbol = self._peek()
        self._eat(symbol)
        return symbol

    # Grammar methods

    def _expression(self):
        return self._parse_keyword(QueryKeyword.NOT, self._disjunction)

    def _disjunction(self):
        return self._parse_keyword(QueryKeyword.OR, self._conjunction)

    def _conjunction(self):
        return self._parse_keyword(QueryKeyword.AND, self._base)

    def _parse_keyword(self, keyword, func):
        expr = func()

        while self._has_next(count=keyword.count()) and self._peek(count=keyword.count()) == keyword.key():
            self._eat(self._peek(count=keyword.count()), count=keyword.count())
            right = func()
            expr = Node(expr, right, keyword)

        return expr

    def _base(self):
        word = ""
        while self._has_next():
            symbol = self._peek()
            if symbol == "(":
                self._eat("(")
                expression = self._expression()
                self._eat(")")
                self._eat_whitespaces()
                return expression
            elif symbol == " ":
                self._eat(symbol)
                if len(word) > 0:
                    break
            elif symbol == ")":
                break
            else:
                word += symbol
                self._eat(symbol)

        self._eat_whitespaces()
        if len(word) == 0:
            raise Exception("Wrong syntax! at (" + str(self._query_count - len(self._query)) + ")")
        return Node(None, None, word)
