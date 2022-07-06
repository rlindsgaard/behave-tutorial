from behave import *
from twentyone import *


@Given('a dealer')
def step_impl(context):
    context.dealer = Dealer()


@given('a {hand}')
def step_impl(context, hand):
    context.dealer = Dealer()
    context.dealer.hand = hand.split(',')


@When('the round starts')
def step_impl(context):
    context.dealer.new_round()


@When('the dealer sums the cards')
def step_impl(context):
    context.dealer_total = context.dealer.get_hand_total()


@Then('the dealer gives itself two cards')
def step_impl(context):
    assert len(context.dealer.hand) == 2


@Then('the {total:d} is correct')
def step_impl(context, total):
    dt = context.dealer_total
    assert dt == total, f'{dt} == {total}'
