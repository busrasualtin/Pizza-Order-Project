# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:16:12 2023

@author: busra
"""

import csv
import datetime

file=open("Menu.txt", "w")
file.write("* Please pick a type of your Pizza:\n")
file.write("1: Classic Pizza\n")
file.write("2: Margarita Pizza\n")
file.write("3: Turkish Pizza\n")
file.write("4: Mexican Pizza\n")
file.write("5: Full Up Pizza\n")
file.write("6: Pizza with Sausage\n")
file.write("7: Meat Pizza\n")
file.write("8: Chicken and Barbeque Pizza\n")
file.write("9: Vegetarian Pizza\n")
file.write("* You have to pick your extra ingredient:\n")
file.write("10: Cheese\n")
file.write("11: Olive\n")
file.write("12: Mushroom\n")
file.write("13: Bacon\n")
file.write("14: Chicken\n")
file.write("15: Veal\n")
file.write("16: Corn\n")
file.write("17: Onion\n")
file.write("* Thanks for choosing your order!\n")

class Pizza:
    #Pizza is the superclass
      def __init__(self,description,cost):
          self.description=description
          self.cost=cost
        
      def get_description(self):
          return self.description
      
      def get_cost(self):
          return self.cost
    


#description and cost
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza with tomato sauce, mozzarella cheese, olive and mushroom", 12.99)
class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza with tomato sauce and mozzarella cheese", 10.99)
class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza with tomato sauce, mozzarella cheese, onion and turkish meat", 17.99)
class MexicanPizza(Pizza):
    def __init__(self):
        super().__init__("Mexican Pizza with tomato sauce, mozzarella cheese, chilli pepper, hot mexican sauce, sausage and sweet pepper", 14.99)
class FullUpPizza(Pizza):
    def __init__(self):
        super().__init__("Full Up Pizza with tomato sauce, mozzarella cheese, olive, mushroom, pepper and sausage", 15.99)
class PizzawithSausage(Pizza):
    def __init__(self):
        super().__init__("Pizza with Sausage, tomato sauce,mozzarella cheese, garlic and basil sauce", 11.99)
class MeatPizza(Pizza):
    def __init__(self):
        super().__init__("Meat Pizza with tomato sauce, mozzarella cheese, pepper, grilled ribs and onion", 18.99)
class ChickenandBarbequePizza(Pizza):
    def __init__(self):
        super().__init__("Chicken and Barbeque Pizza with tomato sauce, mozzarella cheese, chichken and barbeque sauce", 16.99)
class VegetarianPizza(Pizza):
    def __init__(self):
        super().__init__("Vegetarian Pizza with tomato sauce, vegetarian cheese, pepper, carrot, ", 13.99)
        
        
#class Decorator is the super class for extras        
class Decorator(Pizza):
    def __init__(self,pizza):
        self.pizza=pizza
      
    def get_description(self):
        return self.pizza.get_description()
    
    def get_cost(self):
        return self.pizza.get_cost()
      
  



#classes for extras...
class Cheese(Decorator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.description="Cheese"
        self.cost=1.99
      
    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"
      
    def get_cost(self):
        return self.pizza.get_cost() + self.cost
      
   

class Olive(Decorator):
  def __init__(self,pizza):
      super().__init__(pizza)
      self.description="Olive"
      self.cost=0.99

  def get_description(self):
      return f"{self.pizza.get_description()}, {self.description}"

  def get_cost(self):
      return self.pizza.get_cost() + self.cost


class Mushroom(Decorator):
  def __init__(self,pizza):
      super().__init__(pizza)
      self.description="Mushroom"
      self.cost=1.99

  def get_description(self):
      return f"{self.pizza.get_description()}, {self.description}"

  def get_cost(self):
      return self.pizza.get_cost() + self.cost  


class Bacon(Decorator):
  def __init__(self,pizza):
      super().__init__(pizza)
      self.description="Bacon"
      self.cost=2.99

  def get_description(self):
      return f"{self.pizza.get_description()}, {self.description}"

  def get_cost(self):
      return self.pizza.get_cost() + self.cost 


class Chicken(Decorator):
  def __init__(self,pizza):
      super().__init__(pizza)
      self.description="Chicken"
      self.cost=1.99

  def get_description(self):
      return f"{self.pizza.get_description()}, {self.description}"

  def get_cost(self):
      return self.pizza.get_cost() + self.cost 


class Veal(Decorator):
  def __init__(self,pizza):
      super().__init__(pizza)
      self.description="Veal"
      self.cost=2.99

  def get_description(self):
      return f"{self.pizza.get_description()}, {self.description}"

  def get_cost(self):
      return self.pizza.get_cost() + self.cost 


class Corn(Decorator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.description="Corn"
        self.cost=0.99

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost 


class Onion(Decorator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.description="Onion"
        self.cost=0.99

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost
  



def main():
    with open("Menu.txt", "r") as file:
        print(file.read())
    
    print("Please, select your pizza and extra. Write your choices exactly the same as What you see in the menu.")
    pizza_choice = input("Select a pizza: ")
    extra_choice = input("Select an extra: ")
    total_choice=[pizza_choice,extra_choice]
    

    # pizza ve ekstra örneklerini oluşturmak
    
    pizza = None
    if pizza_choice == "Classic Pizza":
        pizza = ClassicPizza()
      

    elif pizza_choice == "Margherita Pizza":
        pizza = MargheritaPizza()
        

    elif pizza_choice == "Turkish Pizza":
        pizza = TurkishPizza()
      

    elif pizza_choice == "Mexican Pizza":
        pizza = MexicanPizza()

    elif pizza_choice == "Full Up Pizza":
        pizza = FullUpPizza()

    elif pizza_choice == "Pizza with Sausage":
        pizza = PizzawithSausage()

    elif pizza_choice == "Meat Pizza":
        pizza = MeatPizza()

    elif pizza_choice == "Chicken and Barbeque Pizza":
        pizza = ChickenandBarbequePizza()

    elif pizza_choice == "Vegetarian Pizza":
        pizza = VegetarianPizza()

    else:
        print("Please give a valid pizza name !")
        return pizza_choice
      
    

    extra = None
    if extra_choice == "Cheese":
        extra = Cheese(pizza)
      
    
    elif extra_choice == "Olive":
        extra = Olive(pizza)
      

    elif extra_choice == "Mushroom":
        extra = Mushroom(pizza)

    elif extra_choice == "Bacon":
        extra = Bacon(pizza)

    elif extra_choice == "Chicken":
        extra = Chicken(pizza)

    elif extra_choice == "Veal":
        extra = Veal(pizza)

    elif extra_choice == "Corn":
        extra = Corn(pizza)

    elif extra_choice == "Onion":
        extra = Onion(pizza)

    else:
        print("Please give a valid extra name !")
        return extra_choice
      

    # toplam fiyatı hesaplamak
    total_cost = pizza.get_cost()
    if extra is not None:
        total_cost += extra.get_cost()
      

    # kullanıcı bilgilerini almak
    name_surname = input("Enter your name and surname: ")
    tcno = input("Enter your tcno: ")
    cardno = input("Enter your card no: ")
    cardkey = input("Enter your card key: ")

    # Şu anki zamanı al
    order_time = datetime.datetime.now()

    

    # Verilerin bir liste olarak saklanması
    data = [total_choice, order_time, name_surname, tcno, cardno, cardkey]
    
    # csv dosyası oluşturma 
    with open('Orders_Database.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Order', 'Date Time', 'Name Surname', 'Tc No', 'Card No', 'Card Key'])
        writer.writerow(data)
      
    
main()
  