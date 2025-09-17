#   class
class Microwave:
    #   constructor with args brand_name,rating
    #   if we didnt create __init__ method(constructor) then python will create default one
    def __init__(self, brand_name: str, rating: int):
        self.brand_name: str = brand_name
        self.rating: int = rating
        #   we need to restrict this from direct use so im using __
        self.__turn_on: bool = False

    def turn_on(self) -> None:
        if self.__turn_on:
            print(f"Microwave is already turned on")
        else:
            self.__turn_on = True
            print(f"Microvave turned on")

    def turn_off(self) -> None:
        if self.__turn_on:
            self.__turn_on = False
            print(f"Microwave is Turned off")
        else:
            print(f"Microvave is already on off")

    def run(self, seconds: int) -> None:
        if self.__turn_on:
            print(f"Run for {seconds} seconds")
        else:
            print(
                f"Encounter an problem please check did the microvave is turned on or not?")

    #   Dunder method
    def __add__(self, other) -> str:
        return f"{self.brand_name} + {other.brand_name}"

    def __str__(self) -> str:
        return f"brand is {self.brand_name} and product rating is {self.rating}"

    def __repr__(self) -> str:
        return f"Microwave(brand_name : '{self.brand_name}', rating : {self.rating})"


#   Object creation
prestige: Microwave = Microwave("Prestige", 3)
bosch: Microwave = Microwave("Bosch", 3)
print(prestige)  # its print like this <__main__.Microwave object at 0x000001520F076A50> same behaviour of java there we will use toString ovveride method to customize our reselt when we pass our object reference name
# similary to achieve like that we have dunder methods which is works like as same as toString() methods its looks like __str__
print(repr(prestige))

#   Accessing variables
print(prestige.brand_name)
print(prestige.rating)
#   here we cannot access the turn_on value if we try we will get error
#   print(prestige.__turn_on)  # AttributeError: 'Microwave' object has no attribute '__turn_on'.
#   if we want to check it we have one solution to check this
print(prestige._Microwave__turn_on)
# _Microwave__turn_on we wont get this as suggestion while writting the code
#   python creates this at the time of compilation

#   method calling
prestige.turn_off()
prestige.turn_on()
prestige.turn_off()
prestige.run(12)
prestige.turn_on()
prestige.run(12)


print(prestige + bosch)
