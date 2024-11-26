from calculator import add, subtract, multiply, divide
from behave import *


@given(u'the calculator is initialized')
def step_impl(context):
    context.calculator = None  # Calculator functions are imported directly

@when(u'I add {a:d} and {b:d}')
def step_impl(context, a, b):
    context.result = add(float(a), float(b))

@when(u'I subtract {a:d} from {b:d}')
def step_impl(context, a, b):
    context.result = subtract(float(b), float(a))

@when(u'I multiply {a:d} and {b:d}')
def step_impl(context, a, b):
    context.result = multiply(float(a), float(b))

@when(u'I divide {a:d} by {b:d}')
def step_impl(context, a, b):
    context.result = divide(float(a), float(b))

@then(u'the result should be {expected_result}')
def step_impl(context, expected_result):
    assert context.result == float(expected_result), f"Expected {expected_result} but got {context.result}"


