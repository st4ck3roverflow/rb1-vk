import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import random

import config
import utils
from logger import log_info, log_error


def check_admin(from_id):
    if len(config.controllers) == 0:
        config.controllers.append(from_id)
        log_info('Added {} to admins due to empty list of admins'.format(from_id))
        return True

    elif from_id in config.controllers:
        return True

    else:
        return False


class RaidBot:
    def __init__(self, token, group_id):
        log_info(config.ver_msg)
        self.vk_session = vk_api.VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk_session, group_id, wait=0.1)
        self.vk = self.vk_session.get_api()
        self.community_info = self.vk.groups.getById(group_id=group_id)
        self.start_listening()

    def start_raid(self, peer_id, controllers):
        working = True
        while working:
            for event in self.longpoll.check():
                # print(event)
                from_id = event.object['message']['from_id']
                message_text = event.object['message']['text']
                if event.type == VkBotEventType.MESSAGE_NEW:
                    parsed_text = utils.parse_message(message_text, self.community_info)
                    if from_id in controllers:
                        if parsed_text == "stopRaid":
                            log_info('{} requested raid stop'.format(from_id))
                            admin_check_answer = check_admin(from_id)
                            if admin_check_answer:
                                config.controllers.append(from_id)
                                log_info('Request approved. Starting raid.')
                                working = False
                                self.vk.messages.send(peer_id=peer_id, message="Raid is stopped",
                                                      random_id=get_random_id())

                            else:
                                log_info("Request denied. {} isn't in admin list.")
                                self.vk.messages.send(peer_id=peer_id, message="No access", random_id=get_random_id())

            if working:
                try:
                    self.vk.messages.send(peer_id=peer_id, message=random.choice(config.msgs),
                                          random_id=get_random_id())
                except vk_api.exceptions.ApiError:
                    working = False
                    log_error('Kicked from conversation, stopping...')

    def start_listening(self):
        for event in self.longpoll.listen():
            # print(event)
            peer_id = event.object['message']['peer_id']
            from_id = event.object['message']['from_id']

            message_text = event.object['message']['text']
            if event.type == VkBotEventType.MESSAGE_NEW:
                if message_text == '':
                    action_type = event.object['action']['type']
                    if action_type == 'chat_invite_user':
                        log_info('Entered conversation')
                # print(message_text)
                parsed_text = utils.parse_message(message_text, self.community_info)
                if parsed_text == "ver":
                    self.vk.messages.send(peer_id=peer_id, message=config.ver_msg, random_id=get_random_id())
                if parsed_text == "startRaid":
                    log_info('{} requested raid start.'.format(from_id))
                    admin_check_answer = check_admin(from_id)
                    if admin_check_answer:
                        config.controllers.append(from_id)
                        log_info('Request approved. Starting raid.')
                        self.start_raid(peer_id=peer_id, controllers=config.controllers)

                    else:
                        log_info("Request denied. {} isn't in admin list.")
                        self.vk.messages.send(peer_id=peer_id, message="No access", random_id=get_random_id())


if __name__ == "__main__":
    rb = RaidBot(config.community_token, config.group_id)

else:
    print("This isn't module! It's standalone script!")
