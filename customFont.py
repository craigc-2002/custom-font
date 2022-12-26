"""
This file contains classes to render text onto a pygame surface and create a custom font from a PNG font sheet
"""
import pygame

"""
TO DO:
- Implement tab
- Implement scaling for different font sizes
- Create full font of characters
"""


class CustomFont:
    """
    class to create a custom font from a PNG font sheet that can then be displayed on screen
    """
    def __init__(self, font_sheet_filepath, font_dict_path):
        """
        Constructor method for the Font class

        Goes through the font sheet and extracts each character according to the data in font_dict
        and stores in a dictionary

        font_dict should take the form:
            {[character]: ((topLeft_x, topLeft_y),(bottomRight_x, bottomRight_y))}

        :param font_sheet_filepath:
        :param font_dict_path:
        """
        self.font_dict = get_dict_from_file(font_dict_path)
        self.font_chars = get_characters(font_sheet_filepath, self.font_dict)

    def render(self, text, font_size):
        """
        Method to render a string and return it as a pygame surface.

        :param text:
        :return text_surf:
        :param font_size:
        """
        scale = (30, 30)
        col = 0
        row = 0

        lines = 1
        cont_line = 0
        longest_line = 0
        for i in text:
            if i == "\n":
                lines += 1
                if cont_line > longest_line:
                    longest_line = cont_line
            elif i == "\t":
                cont_line = 4
            else:
                cont_line += 1

        text_surface = pygame.Surface((longest_line*scale[0], lines*scale[1]), flags=pygame.SRCALPHA)
        text_surface.fill((0, 0, 0, 0))
        display_char = pygame.transform.scale(self.font_chars["unknown_character"], scale)

        for i in text:
            if i in self.font_chars:
                display_char = pygame.transform.scale(self.font_chars[i], scale)
            elif i == "\n":
                row += 1
                col = -1
            elif i == "\t":
                col += 1

            display_pos = (col * scale[0], row * scale[1])
            text_surface.blit(display_char, display_pos)
            col += 1

        return text_surface

    def write(self, text, display_surface, font_size, position, ref_point="corner"):
        """
        Method to call the render method for a text string and display it on the screen.

        :param text:
        :param display_surface:
        :param font_size:
        :param position:
        :param ref_point:
        """
        text_surface = self.render(text, font_size)
        blit_position = position
        if ref_point == "centre":
            blit_position = (blit_position[0] - text_surface.get_width()/2,
                             blit_position[1] - text_surface.get_height()/2)

        display_surface.blit(text_surface, blit_position)


def get_characters(image_path, font_index):
    """
    Method to take in the overall font image and split it into images for each character according to the
    font index dictionary

    Image index takes the format of a dictionary with the name of the character as the key and a list of two corners
    as the value.

    Image index takes the form;
        {"character_name":((corner_1x, corner_1y), (corner_2x, corner_2y))}
    :param image_path:
    :param font_index:
    :return sprites:
    """
    full_image = pygame.image.load(image_path)
    full_image = full_image.convert_alpha(full_image)
    characters = {}

    for sprite in font_index:
        img_data = font_index[sprite]

        width = img_data[1][0] - img_data[0][0]
        height = img_data[1][1] - img_data[0][1]
        blit_pos = (-img_data[0][0], -img_data[0][1])

        sprite_image = pygame.Surface((width, height), flags=pygame.SRCALPHA)
        sprite_image.fill((0, 0, 0, 0))
        sprite_image.blit(full_image, blit_pos)
        sprite_image = sprite_image.convert_alpha(sprite_image)

        characters[sprite] = sprite_image

    return characters


def get_dict_from_file(filepath):
    """
    Function to convert the data stored in a text file to a dictionary that can be used by a CustomFont object
    to extract the characters from a font sheet.

    :param filepath:
    :return font_dict:
    """
    file_text = ""

    with open(filepath) as f:
        for line in f:
            file_text += line

    font_dict = eval(file_text)

    return font_dict
