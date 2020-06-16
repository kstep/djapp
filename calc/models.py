from django.db import models

import operator as op
import math

# Create your models here.


class Op:
    def __init__(self, func, prio, arity=2, left_as=False):
        self.left_assoc = left_as
        self.priority = prio
        self.function = func
        self.arity = arity

    def __call__(self, stack):
        nargs = self.arity
        result = self.function(*stack[-nargs:])
        if result is not None:
            stack[-nargs:] = [result]

    def ready(self, other):
        return (other.priority > self.priority or
                other.priority == self.priority and self.left_assoc)


class Expr(models.Model):
    name = models.CharField(max_length=200, blank=True, default="")
    result = models.FloatField(null=True)
    expression = models.CharField(max_length=500)

    operators = {
        '^': Op(op.pow, 3, left_as=True),
        '*': Op(op.mul, 2),
        '/': Op(op.truediv, 2),
        '%': Op(op.mod, 2),
        '+': Op(op.add, 1),
        '-': Op(op.sub, 1),

        'sin': Op(math.sin, 4, 1),
        'cos': Op(math.cos, 4, 1),
        'tg': Op(math.tan, 4, 1),
        'ctg': Op(lambda x: 1 / math.tan(x), 4, 1),
        'log': Op(math.log2, 4, 1),
        'log10': Op(math.log10, 4, 1),
        'lnp1': Op(math.log1p, 4, 1),
    }

    def calculate(self):
        out_stack = []
        op_stack = []

        expr = self.expression.split()
        for token in expr:
            if token.isnumeric():
                out_stack.append(float(token))
            elif token in self.operators:
                op = self.operators[token]
                while op_stack and op_stack[-1] != '(' and op.ready(op_stack[-1]):
                    op_stack.pop()(out_stack)
                op_stack.append(op)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                while op_stack and op_stack[-1] != '(':
                    op_stack.pop()(out_stack)
                if out_stack[-1] == '(':
                    out_stack.pop()

        while op_stack:
            op = op_stack.pop()
            if op != '(':
                op(out_stack)

        return ", ".join(map(str, out_stack))


