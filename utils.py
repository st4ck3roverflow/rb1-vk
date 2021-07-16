import config


def adjust_message_text(msg):
    msg_space = msg + " "
    message_text = msg_space.encode()
    if len(message_text) < 4096:
        message_text = message_text * int(4096 / len(message_text))
        return message_text.decode()


def parse_message(message_text, community_info):
    screen_name = community_info[0]['screen_name']
    name = community_info[0]['name']
    group_id = "club" + str(config.group_id)
    vk_prefix1 = ('[' + group_id + '|@' + screen_name).replace(' ', '')
    vk_prefix2 = ('[' + group_id + '|' + name).replace(' ', '')

    splited_message = message_text.replace(' ', '').split(']')
    if str(splited_message[0]) == str(vk_prefix1) or str(splited_message[0]) == str(vk_prefix2):
        return splited_message[1]
    else:
        return False

