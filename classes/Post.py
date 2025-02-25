import pygame

from classes.constants import *
from helpers import screen


class Post:
    
    def __init__(self, username, location, description, like_counter, comments):
        self.username = username
        self.location = location
        self.description = description
        self.like_counter = like_counter
        self.comments = comments

    def add_like(like_counter):
        like_counter += 1

    def add_comments(comments):
        comments = input("Enter your comments: ")
        

    def display(username, location, description, like_counter, comments):
        global screen
        screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        screen = pygame.display.set_mode(screen_size)

        font = pygame.font.SysFont(username, UI_FONT_SIZE)
        text = font.render(username, True, BLACK)
        screen.blit(text, [USER_NAME_X_POS, USER_NAME_Y_POS])

        font = pygame.font.SysFont(location, UI_FONT_SIZE)
        text = font.render(location, True, BLACK)
        screen.blit(text, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

        font = pygame.font.SysFont(like_counter, UI_FONT_SIZE)
        text = font.render(username, True, BLACK)
        screen.blit(text, [LIKE_TEXT_X_POS, LIKE_BUTTON_Y_POS])

        font = pygame.font.SysFont(description, UI_FONT_SIZE)
        text = font.render(username, True, BLACK)
        screen.blit(text, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        font = pygame.font.SysFont(comments, UI_FONT_SIZE)
        text = font.render(comments, True, BLACK)
        screen.blit(text, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        pygame.display.flip()
        


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break


class ImagePost(Post):
    def __init__(self, username, location, description, like_counter, comments, image):
        super().__init__(username, location, description, like_counter, comments)
        self.image = image

    def display(image):
        super().display

        img = pygame.image.load(image)
        img = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))
        screen.blit(img, (POST_X_POS, POST_Y_POS))
        pygame.display.flip()

class TextPost(Post):
    def __init__(self, username, location, description, like_counter, comments, text, text_color, background_color):
        super().__init__(username, location, description, like_counter, comments)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    def display(text, text_color, background_color):
        super().display

        font = pygame.font.SysFont(text, TEXT_POST_FONT_SIZE)
        text = font.render(text, True, text_color)
        screen.blit(text, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])
        pygame.display.flip()

class Comment():
    def __init__(self, comment, respond_counter):
        self.comment = comment
        self.respond_counter = respond_counter

    def display_comments():
        pass

