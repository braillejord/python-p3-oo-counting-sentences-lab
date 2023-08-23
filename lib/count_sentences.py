#!/usr/bin/env python3


class MyString:
    def __init__(self, value=" "):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return True if self.value.endswith(".") else False
