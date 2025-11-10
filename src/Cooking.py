import pygame
 

# class click():
    # def __init__(image, exit_rect):
        #exit_rect = pygame.Rect((455, 900), (1080, 1023))

    #def track_mouse():
        #for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #mouse_pos = pygame.mouse.get_pos()
    
    #def exit_button(mouse_pos):
        



    
    # this makes each area individully clickable
    
    # def mouse_location():
        #mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos[0])
    
    #def mouse_print(self):
        #for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if self.
                #print(f"mouse clicked at: {event.pos}")

#  class backdrop():
    # this will change the background

def main():
    pygame.init()
    pygame.display.set_caption("Make that Pancake!")
    resolution = (1500, 1048)
    screen = pygame.display.set_mode(resolution)
    title = pygame.image.load('Images/Title_screen.png')
    home_screen = pygame.image.load('Images/Resized.png')
    black = pygame.Color(0, 0, 0)
    screen.fill(black)
    screen.blit(title, (0,0))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse clicked")
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos[0])
                print(mouse_pos[1])
                screen.blit(home_screen, (0, 0))
                pygame.display.flip()
            if event.type == pygame.quit:
                running = False

if __name__ == "__main__":
    main()