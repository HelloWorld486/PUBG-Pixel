#PUBG Pixel main
#by xkcdjerry and HelloWorld486
#Pixel clone of game PUBG
import abc,collections

import pygame

from classlib import Root

TESTING=True
pygame.init()
imgs={}#stub
_cache={}

def cache(name:str) -> pygame.image:
    pass #return pygame.image


class Game:
    def __init__(self) -> None:
        #stub
        self.keys={}
        self.rewind()
        #init game(using rewind)
    def rewind(self) -> None:
        #stub
        player=Player()#TODO
        self.entitys=collections.deque([player,Blood_bar(player)])
        #init the parts of the game that needs to be reset each round
    def quit(self):
        pass#quit the game
    def run(self) -> bool:
        'return True if run again,else False'
        while True:
            for event in pygame.event.get():
                pass#handle event
            self.update()
    def update(self):
        #stub

        #some game code
        
        for i in self.entitys:
            i.update(self)
        self.render()
    def render(self):
        self.window.blit(BG)
        for i in self.entitys:
            img,rect=i.render()
            self.window.blit(img,rect)

            
class Entity(Root):
    "Base class for game objects"
    @abc.abstractmethod
    def __init__(self,img_name,pos):
        self.img_name=img_name
        self.img=cache(img_name)
        self.rect=self.img.get_rect()
        self.rect.center=pos

    @abc.abstractmethod
    def update(self,game):
        "update self with arg name"
        pass#update self according to game
    
    @abc.abstractmethod
    def render(self,game):
        "return tuple img,rect"
        pass#return tuple img,rect
class Player(Entity):
    pass#TODO stub
class Blood_bar(Entity):
    def __init__(self,player):
        pass#TODO stub
    def update(self,game):
        pass

def main():
    game=Game()
    while game.run():
        game.rewind()
    game.quit()
if __name__=="__main__" and not TESTING:
    main()
