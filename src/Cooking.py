import pygame
 

# class recipe():
    # list all ingredients
    

class ingredients():
     
    def draw():
        Egg_test = pygame.image.load('Images/Egg_Image.png')
        resolution = (1500, 1048)
        screen = pygame.display.set_mode(resolution)


    # def is_clicked():

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
    title = pygame.image.load('Images/Title_screen.png')
    home_screen = pygame.image.load('Images/First_Screen.png')
    black = pygame.Color(0, 0, 0)
    screen.fill(black)
    screen.blit(title, (0,0))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > 455 and mouse_pos[0] < 1018 and mouse_pos[1] > 900 and mouse_pos[1] < 1023:
                        running = False
                print(mouse_pos[0])
                print(mouse_pos[1])
                screen.blit(home_screen, (0, 0))
                pygame.display.flip()
            if event.type == pygame.quit:
                running = False

if __name__ == "__main__":
    main()