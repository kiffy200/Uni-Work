#!/usr/bin/env python3
class Money:
    def __init__(self, anAmount, aCurrency):
        self.amount = anAmount
        self.currency = aCurrency
    def __str__(self):
        return str(self.amount) + ' ' + self.currency
    def convert(self, rateFromTo, newCurrency):
        newAmount = self.amount*rateFromTo
        self.amount = round(newAmount)
        self.currency = newCurrency
    def times(self, multi):
        nextamount = self.amount*multi
        self.amount = nextamount

money1 = Money(int(input('Enter Pounds ')), 'GDP')
print(money1)
money1.convert(1.64, 'USA')
print(money1)
money1.times(4)
print(money1)
