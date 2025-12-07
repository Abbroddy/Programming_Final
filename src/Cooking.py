import pygame


class bowl():

    def __init__(self, screen):
        self.ing = ["egg", "oil", "water", "mix"]
        self.add_ing = [False, False, False, False]
        # self.img_place = ['Images/Egg_Image.png', 'Images/Egg_Image.png', 'Images/Egg_Image.png', 'Images/Egg_Image.png']
        self.image = [pygame.image.load('Images/Egg_Bowl.png'), pygame.image.load('Images/Bowloil.png'), pygame.image.load('Images/Bowlwater.png'), pygame.image.load('Images/Bowlmix.png')]
        self.loc = [(470, 321), (670, 372), (968, 304), (750, 354)]
        self.screen = screen

    def ingredient_clicked(self, name):
        good_ing = True
        if name in self.ing:
            position = self.ing.index(name)
            self.add_ing[position] = True
        else:
            good_ing = False
        return good_ing
    
    def draw(self):
        for index in range(len(self.ing)):
            if self.add_ing[index] == True:
                self.screen.blit(self.image[index], self.loc[index])

    def is_done(self):
        done = True
        for item in self.add_ing:
            if item == False:
                done = False
        return done
    
    def reset(self):
        self.add_ing = [False, False, False, False]
    

class Ingredient():

    def __init__(self, x, y, filename, screen, name):
        self.screen = screen
        self.x = x
        self.y = y
        self.filename = filename
        self.name = name
        self.visible = True
        self.image = pygame.image.load(filename)
        self.restart = False

    def draw(self):
        if self.visible == True:
            self.screen.blit(self.image, (self.x, self.y))
            
    def is_clicked(self, mouse_x, mouse_y):
        wasclicked = False 
        width = self.image.get_width()
        height = self.image.get_height()
        x2 = (self.x + width) 
        y2 = (self.y + height)
        if mouse_x > self.x and mouse_x < x2 and mouse_y > self.y and mouse_y < y2:
            self.visible = False
            wasclicked = True
        return wasclicked
    
    def reset(self):
        self.visible = True 

def main():
    pygame.init()
    pygame.display.set_caption("Make that Pancake!")
    resolution = (1500, 1048)
    screen = pygame.display.set_mode(resolution)
    the_bowl = bowl(screen)

    ing_list = []
    ing1 = Ingredient(50, 750, 'Images/Egg_Image.png', screen, "egg")
    ing2 = Ingredient(1100, 5, 'Images/Veg_Oil.png', screen, "oil")
    ing3 = Ingredient(1400, 5, 'Images/Water.png', screen, "water")
    ing4 = Ingredient(700, 1, 'Images/Mix.png', screen, "mix")
    ing5 = Ingredient(400, 1, 'Images/Carrot.png', screen, "carrot")
    ing6 = Ingredient(100, 400, 'Images/Cat_Food.png', screen, "cat food")
    ing7 = Ingredient(50, 10, 'Images/Ketchup.png', screen, "ketchup")
    ing8 = Ingredient(1250, 350, 'Images/Soda.png', screen, "soda")
    ing_list.append(ing1)
    ing_list.append(ing2)
    ing_list.append(ing3)
    ing_list.append(ing4)
    ing_list.append(ing5)
    ing_list.append(ing6)
    ing_list.append(ing7)
    ing_list.append(ing8)


    title = pygame.image.load('Images/Title_screen.png')
    black = pygame.Color(0, 0, 0)
    screen.fill(black)
    screen.blit(title, (0,0))
    pygame.display.flip()
    pygame.time.delay(100)
    #4000

    home_screen = pygame.image.load('Images/First_Screen.png')
    Lose_img = pygame.image.load('Images/Lose.png')
    Win_img = pygame.image.load('Images/Win.png')

    running = True
    while running:

        screen.blit(home_screen, (0, 0))
        for item in ing_list:
            item.draw()
        the_bowl.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()
                #print(mouse_pos)

                if mouse_pos[0] > 455 and mouse_pos[0] < 1018 and mouse_pos[1] > 900 and mouse_pos[1] < 1023:
                        running = False

                for item in ing_list:
                    if item.is_clicked(mouse_pos[0], mouse_pos[1]):
                        print(item.name)
                        good_ingredient = the_bowl.ingredient_clicked(item.name)
                        if good_ingredient == False:
                            the_bowl.reset()
                            for item in ing_list:
                                item.reset()
                            screen.blit(Lose_img, (0,0))
                            pygame.display.flip()
                            pygame.time.delay(4000)
                        else: 
                            if the_bowl.is_done() == True:
                                the_bowl.reset()
                                for item in ing_list:
                                    item.reset()
                                screen.blit(Win_img, (0,0))
                                pygame.display.flip()
                                pygame.time.delay(4000)


            if event.type == pygame.quit:
                running = False


if __name__ == "__main__":
    main()