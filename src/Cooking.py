import pygame
 

# class bowl():
    # list all ingredients
    

class Ingredient():

    def __init__(self, x, y, filename, screen, name):
        self.screen = screen
        self.x = x
        self.y = y
        self.filename = filename
        self.name = name
        self.visible = True
        self.image = pygame.image.load(filename)
     
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
    # def reset():
        



    
    # this makes each area individully clickable
    
    # def mouse_location():
        #mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos[0])
    
    #def mouse_print(self):
        #for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if self.
                #print(f"mouse clicked at: {event.pos}")

def main():
    pygame.init()
    pygame.display.set_caption("Make that Pancake!")
    resolution = (1500, 1048)
    screen = pygame.display.set_mode(resolution)

    ing_list = []
    ing1 = Ingredient(2, 1, 'Images/Egg_Image.png', screen, "Egg")
    ing2 = Ingredient(1264, 1, 'Images/Egg_Image.png', screen, "Oil")
    ing3 = Ingredient(1264, 351, 'Images/Egg_Image.png', screen, "Water")
    ing4 = Ingredient(550, 1, 'Images/Egg_Image.png', screen, "Mix")
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
            if event.type == pygame.quit:
                running = False

if __name__ == "__main__":
    main()