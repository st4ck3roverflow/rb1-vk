import config


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
