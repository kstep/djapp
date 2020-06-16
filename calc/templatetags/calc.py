from django.template import Library, Node
from . import models

register = Library()


@register.tag
def calc(parser, token):
    nodes = parser.parse(('endcalc',))
    parser.delete_first_token()
    return CalcNode(nodes)


class CalcNode(Node):
    def __init__(self, nodes):
        self.nodes = nodes

    def render(self, context):
        expr = models.Expr(expression=self.nodes.render(context))
        return expr.calculate()
