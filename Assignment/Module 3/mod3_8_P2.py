class liquid:
    def prop(self):
        return "Is Liquid"

class water(liquid):
    def prop(self):
        prop = super().prop()
        return f"{prop}, and is Transparent"

w1 = water()
print(w1.prop())