import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

def normalize(size, coordinate, x_or_y):
    if x_or_y == 'x':
        number = size[0] * (coordinate / 560.0)
    else:
        number = size[1] * (coordinate / 840.0)
    return int(number)

def init_and_resize_image(filename, size):
    return pygame.transform.scale(pygame.image.load(filename), size)


#THIS ONE WILL NEED SOME MODIFICATION IT WILL ONLY WORK WITH SELF THAT HAS THE FOLLOWING
#SELF.SIZE
#SELF.SCREEN
#SELF.BACKBUTTONBLACK
#SELF.BACKBUTTONBLUE
def make_back(self, event):
    back_pressed=True
    mouse = pygame.mouse.get_pos()
    x_center = normalize(self.size, 30, 'x')
    y_center = normalize(self.size, 30, 'y')
    side = 40
    coordinates_button=(x_center-(side/2), y_center-(side/2))
    #print("between "+str(x_center-radius) +" and " + str(x_center+radius) + " andBetween " + str(y_center-radius) +" and " + str(y_center+radius))
    if (x_center-(side/2) < mouse[0] < x_center+(side/2)) and (y_center-(side/2) < mouse[1] < y_center+(side/2)):
        self.screen.blit(self.backButtonBlue, coordinates_button)
        if event.type == pygame.MOUSEBUTTONDOWN: return back_pressed
        else: return not back_pressed
    else:
        self.screen.blit(self.backButtonBlack, coordinates_button)
        return not back_pressed


def make_question(self):
    def split_question_print_text(text, arr):
        if (len(text) > 25 and text.find(' ', 21) != -1):
            num = text.find(' ', 25) if 0 < text.find(' ', 25) <= 26 else text.find(' ', 21)
            arr.append(self.calibri_35.render(text[:num], True, BLACK))
            return split_question_print_text(text[num:], arr)
        else:
            arr.append(self.calibri_35.render(text, True, BLACK))
            return arr

    base_q_coordinates = [X, Y] = [60, 290]
    augment_coordinates = [Xa, Ya] = [0, 32]
    text = self.questions[self.q_count].get_question() if self.q_count < len(
        self.questions) else  "Finished, Hope you passed."
    print_statement = split_question_print_text(text, [])
    for i in range(0, len(print_statement)):
        self.screen.blit(print_statement[i], [X, Y + Ya * i])