from lib2to3.refactor import _Driver
from pyexpat import model
from car import Car

class UberX(Car):
    brand = str
    model = str

    def __init__(self, license, driver, brand, model):
        super.__init__(license,driver)
        self.brand = brand
        self.model = model