class Robot:
    level = 0
    
    def __init__(self, name):
        self.name = name

    def speak(self, msg):
        print(msg)

    def walk(self):
        print(f'{self.name} walks')

# modifying an attribute
Robot.level = 10
bot = Robot('PooPoo')

# modifying speak
def add_method(cls):
    '''solution 1:'''
    # @staticmethod
    def speak(cls, msg):
        print(f'{cls.name} says {msg}')

    cls.speak = speak
    
    '''solution 2:'''
    cls.speak = lambda self, msg: print(msg)
    return cls

# modifying __init__
def modify_init(cls):
    def __init__(cls, name, build_yr):
        cls.name = name
        cls.build_yr = build_yr
    
    cls.__init__ = __init__
    
    return cls


Robot = add_method(Robot)
Robot = modify_init(Robot)

bot1 = Robot('Boop', 2014)
bot1.walk()
bot1.speak('Hi')
