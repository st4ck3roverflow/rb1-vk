from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random


def gen(button_txt):
    kbs = VkKeyboard(one_time=False)
    a, b = 0, 0
    while a <= 9:
        while b <= 2:
            b += 1
            kbs.add_button(button_txt, random.choice(
                [VkKeyboardColor.NEGATIVE, VkKeyboardColor.POSITIVE, VkKeyboardColor.PRIMARY]))
        if a != 9:
            kbs.add_line()
            a += 1
            b = 0
        else:
            a = 10
    return kbs.get_keyboard()
