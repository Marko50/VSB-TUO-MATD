from query_parser import QueryParser
from query_keyword import QueryKeyword
from node import Node
from tree_search import TreeSearch

def rebuild_expression(tree, inverted_index):
    stack = []
    expression_stack = []

    def tree_search_callback(node):
        if node.is_leaf():
            stack.append(node.data)
            expression_stack.append(inverted_index[node.data])
            return
#
        if node.data == QueryKeyword.AND:
            second = stack.pop()
            first = stack.pop()
            expr = "(" + first + " AND " + second + ")"
            stack.append(expr)
            
            second_exp_stack = expression_stack.pop()
            first_exp_stack = expression_stack.pop()
            expression_stack.append(list(set(first_exp_stack) & set(second_exp_stack)))
        elif node.data == QueryKeyword.OR:
            second = stack.pop()
            first = stack.pop()
            expr = "(" + first + " OR " + second + ")"
            stack.append(expr)

            second_exp_stack = expression_stack.pop()
            first_exp_stack = expression_stack.pop()
            expression_stack.append(list(set(first_exp_stack) | set(second_exp_stack)))
        elif node.data == QueryKeyword.NOT:
            second = stack.pop()
            first = stack.pop()
            expr = "(" + first + " NOT " + second + ")"
            stack.append(expr)

            second_exp_stack = expression_stack.pop()
            first_exp_stack = expression_stack.pop()
            expression_stack.append(list(set(first_exp_stack) - set(second_exp_stack)))

    tree_search = TreeSearch(tree)
    tree_search.depth_first(tree_search_callback)
    return (stack.pop()),(expression_stack.pop())


# try:            print(first + " NOT " + second)
#     parser = QueryParser(query)
#     tree = parser.parse()
#     print("Original Query:")
#     print(query)
#     print("Rebuilt Query:")
#     expression = rebuild_expression(tree)
#     print(expression)
# except Exception as e:
#     print(e)
