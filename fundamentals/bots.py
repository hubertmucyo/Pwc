#this program simply explores class and object variables
# It is a program that takes the name of robot and print 
# keeping count of their population
 
class robot:
    population = 0

    def __init__(self,name):
        self.name = name
        print("Initializing {}".format(self.name))
        robot.population += 1

    def die(self):
        print("{} is being destroyed".format(self.name))
        robot.population -= 1

        if robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("there are still {:d} robots working".format(robot.population))

    def sayhi(self):
        print("Hello, my masters call me: {}".format(self.name))

    def how_many(obj):
        print("we have {} robots".format(obj.population))

b1 = robot("chat-Gpt")
b1.sayhi()
b1.how_many()
print("{} has started working".format(b1))

b2 = robot("grok")
b2.sayhi()
b2.how_many()
print("{} has also started working".format(b2))

print("The bots have finished the work assigned")
b1.die()
b2.die()