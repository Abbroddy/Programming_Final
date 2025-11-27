import pygame


class bowl():

    def __init__(self, screen):
        self.ing = ["egg", "oil", "water", "mix"]
        self.add_ing = [False, False, False, False]
        # self.img_place = ['Images/Egg_Image.png', 'Images/Egg_Image.png', 'Images/Egg_Image.png', 'Images/Egg_Image.png']
        self.image = [pygame.image.load('Images/Egg_Image.png'), pygame.image.load('Images/Egg_Image.png'), pygame.image.load('Images/Egg_Image.png'), pygame.image.load('Images/Egg_Image.png')]
        self.loc = [(500, 200), (500, 400), (500, 600), (500, 20)]
        self.screen = screen

    def ingredient_clicked(self, name):
        good_img = True
        if name in self.ing:
            position = self.ing.index(name)
            self.add_ing[position] = True
        else:
            good_img = False
        print(self.add_ing)
        return good_img
        



        # good_ing = true
        # if name part of self.ing, 
        #   set add_ing = true
        # if name not in list,
        #   good_ing = false
        #   return fail

        # below goes in main when ing clicked

        # if bowl.ingredient_clicked(name) = true
        #   N/A
        
        # else: bad things ooooo
    
    def draw(self):
        #print(self.ing)
        #print(self.loc)
        print(self.add_ing)
        for index in range(len(self.ing)):
            #print(index)
            if self.add_ing[index] == True:
                self.screen.blit(self.image[index], self.loc[index])
        #   draw it

    # list all ingredient
    

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
    ing1 = Ingredient(2, 1, 'Images/Egg_Image.png', screen, "egg")
    ing2 = Ingredient(1264, 1, 'Images/Egg_Image.png', screen, "oil")
    ing3 = Ingredient(1264, 351, 'Images/Egg_Image.png', screen, "water")
    ing4 = Ingredient(550, 1, 'Images/Egg_Image.png', screen, "mix")
    ing_list.append(ing1)
    ing_list.append(ing2)
    ing_list.append(ing3)
    ing_list.append(ing4)


    title = pygame.image.load('Images/Title_screen.png')
    black = pygame.Color(0, 0, 0)
    screen.fill(black)
    screen.blit(title, (0,0))
    pygame.display.flip()
    pygame.time.delay(4000)

    home_screen = pygame.image.load('Images/First_Screen.png')

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
                print(mouse_pos)

                if mouse_pos[0] > 455 and mouse_pos[0] < 1018 and mouse_pos[1] > 900 and mouse_pos[1] < 1023:
                        running = False

                for item in ing_list:
                    if item.is_clicked(mouse_pos[0], mouse_pos[1]):
                        print(item.name)
                        fred = the_bowl.ingredient_clicked(item.name)

            if event.type == pygame.quit:
                running = False

if __name__ == "__main__":
    main()