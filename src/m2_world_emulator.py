from turtle import Screen, Turtle
from random import Random
import time
import threading
import sys

# The two methods bello convert coordinate to a more logical canvas:
def x_conv(pos_x):
    return pos_x - ( world_width / 2 )

def y_conv(pos_y):
    return ( -pos_y + world_height ) - ( world_height / 2 )

def coordinate_converter( (pos_x, pos_y) ):
    return ( (pos_x - ( world_width / 2 )), ( -pos_y + world_height ) - ( world_height / 2 ) )

class Random_Gen(object):
    def __init__(self, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height
            
    def get_pos(self):
        random_x = Random().randrange(0, self.world_width)
        random_y = Random().randrange(0, self.world_height)
        return coordinate_converter( (random_x, random_y) )

    def get_direction(self):
        return ( Random().randrange(0, 8) )



class World_Time(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.time = 0
        
    def run(self):
        while True:
            time.sleep(0.1)
            self.time += 1
            
    def get_time(self):
        return self.time
    
class God(object):
    def __init__(self, name):
        self.time = 0
        self.casuality = 0
        self.name = name
        
    def create_world(self, size_x, size_y):
        self.world_size_x = size_x
        self.world_size_y = size_y
        self.world_one = World(1, size_x, size_y )
        
    def show_world(self):
        self.world_one.show_world()
        
    def create_material(self):
        self.material = Material()
        
    def create_city_blocks(self, amount_of_blocks_x, amount_of_blocks_y, margin_left_right, margin_top_bottom, road_width, sidewalk_width):
        available_size_x = self.world_size_x - ( margin_left_right * 2 ) - ( (amount_of_blocks_x + 1) * road_width ) - ( ( amount_of_blocks_x * 2 ) * sidewalk_width )
        available_size_y = self.world_size_y - ( margin_top_bottom * 2 ) - ( (amount_of_blocks_y + 1) * road_width ) - ( ( amount_of_blocks_y * 2 ) * sidewalk_width )
        
        building_side_x = available_size_x / amount_of_blocks_x
        building_side_y = available_size_y / amount_of_blocks_y
        
        self.material.build_box(0, 0, self.world_size_x, self.world_size_y, False, "black")
        self.material.build_box(margin_left_right, margin_top_bottom, self.world_size_x - margin_left_right * 2, self.world_size_y - margin_top_bottom * 2, False, "black")
        
        #self.material.draw_line()
        
        for x in range(0, amount_of_blocks_x, 1):
            pos_x = ( margin_left_right + road_width + sidewalk_width ) + x * ( building_side_x + 2 * sidewalk_width + road_width ) 
              
            for y in range(0, amount_of_blocks_y, 1):
                pos_y = ( margin_top_bottom + road_width + sidewalk_width ) + y * ( building_side_y + 2 * sidewalk_width + road_width ) 
              
                self.material.build_box(pos_x - sidewalk_width, pos_y - sidewalk_width, building_side_x + sidewalk_width * 2, building_side_y + sidewalk_width * 2, True, "Gray")              
                self.material.build_box(pos_x, pos_y, building_side_x, building_side_y, True, "black")
                
    def create_time(self):
        self.timer = World_Time()
        self.timer.start()
    
    def create_casuality(self):
        return 0
    
    def get_time(self):
        return self.timer.get_time()
    
    def create_humans(self, number_of_humans):
        for x in range(0, number_of_humans):
            position_x, position_y = random_gen.get_pos()
            
            human = Human(0, 100, 100, (position_x, position_y))
            stampid = self.material.draw_human(position_x, position_y)
            humans.append( (human, stampid, (position_x, position_y) ) )
            
    def slowly_kill_humans(self):
        for human in humans:
            time.sleep(1)
            cur_human, stampid, position = human
            #print cur_human
            #print stampid
            #print position[0], position[1]
            self.material.erase_human(stampid)
            
    def move_humans(self):
        for human in humans:
            return 0

class Material(object):
    def __init__(self):
        self.gods_hand = Turtle()
        self.gods_hand.hideturtle()
        self.gods_hand.speed(0)
        
    def draw_line(self):
        self.gods_hand.penup()
        self.gods_hand.tracer(0, 0)
        self.gods_hand.goto(100, 100)
        self.gods_hand.pendown()
        self.gods_hand.fill(True)
        self.gods_hand.setheading(0)
        self.gods_hand.forward(50)
        self.gods_hand.setheading(90)
        self.gods_hand.forward(50)
        self.gods_hand.setheading(180)
        self.gods_hand.forward(50)
        self.gods_hand.setheading(270)
        self.gods_hand.forward(50)
        self.gods_hand.fill(False)
        self.gods_hand.penup()
        self.gods_hand.goto(120, 120)
        self.gods_hand.pendown()
        self.gods_hand.pencolor("Blue")
        self.gods_hand.fillcolor("Blue")
        self.gods_hand.fill(True)
        self.gods_hand.setheading(0)
        self.gods_hand.forward(10)
        self.gods_hand.setheading(90)
        self.gods_hand.forward(10)
        self.gods_hand.setheading(180)
        self.gods_hand.forward(10)
        self.gods_hand.setheading(270)
        self.gods_hand.forward(10)
        
        self.gods_hand.fill(False)
        self.gods_hand.penup()
        self.gods_hand.tracer(1, 1)
        
    def build_box(self, pos_x, pos_y, length_x, length_y, do_fill, color):
        pos_x, pos_y = coordinate_converter((pos_x, pos_y))
        
        self.gods_hand.tracer(0, 0)
        
        self.gods_hand.penup()
        self.gods_hand.goto(pos_x, pos_y)
        self.gods_hand.pendown()
        
        if do_fill:
            self.gods_hand.fill(True)
            
        self.gods_hand.color(color)
            
        for x in range(4, 0, -1):
            heading = x * 90
            self.gods_hand.setheading(heading)    
            self.gods_hand.forward(length_x)
        
        if do_fill:
            self.gods_hand.fill(False)
        
        self.gods_hand.tracer(1, 1)
                 
    def draw_human(self, pos_x, pos_y):
        self.gods_hand.tracer(0, 0)
        self.gods_hand.penup()
        self.gods_hand.goto(pos_x, pos_y)
        self.gods_hand.color("blue")
        self.gods_hand.shape("circle")
        self.gods_hand.shapesize(0, 0, 5)
        stampid = self.gods_hand.stamp()
        self.gods_hand.color("black")
        self.gods_hand.tracer(1, 1)
        return stampid
        
    def erase_human(self, stampid):
        self.gods_hand.clearstamp(stampid)
        
class World(object):
    def __init__(self, index, size_x, size_y):
        self.index = index
        self.canvas = Screen()
        self.canvas.setup(size_x, size_y)

    def show_world(self):
        #self.canvas.ontimer(god.slowly_kill_humans(), 100)
        self.canvas.exitonclick()
        

class Human(object):
    def __init__(self, human_type, intelligence, activity_level, position):
        self.intelligence = intelligence
        self.activity_level = activity_level
        self.destination = random_gen.get_pos()
        self.direction = "None"
        self.position = position
        
    def get_destination(self):
        return self.destination
    
    def get_direction(self):
        return self.direction


world_width = 700
world_height = 700
number_of_humans = 20
random_gen = Random_Gen(world_width, world_height)
humans = []
god = God("george")

def main():
    god.create_world(world_width, world_height)
    god.create_material()
    god.create_time()
    god.create_city_blocks(5, 5, 20, 20, 20, 15)
    god.create_humans(number_of_humans)
    god.show_world()
    
if __name__ == '__main__': 
    main()