import os
import utils

ver_msg = 'Raid bot community - v0.1 alpha - arturyudin.site - [club199568112|pwned solutions]'

isHerokuInstance = False

if isHerokuInstance:
    community_token = os.environ.get('vk_api_token')
    group_id = os.environ.get('vk_group_id')
    message1 = utils.adjust_message_text(os.environ.get('message1'))
    message2 = utils.adjust_message_text(os.environ.get('message2'))
    message3 = utils.adjust_message_text(os.environ.get('message3'))
    msgs = [message1, message2, message3]
    controllers = os.environ.get('admins')

else:
    community_token = "85f72365ea4c87422f30f995e7078efc179a99ffb7d3be96e081c09f683bd62ba4bc7adc32aa7da9caeaa"  # group token
    group_id = 199568112  # vk group id without club
    message1 = utils.adjust_message_text("pwned.solution test msg1")
    message2 = utils.adjust_message_text("pwned.solution test msg2")
    message3 = utils.adjust_message_text("pwned.solution test msg3")
    msgs = [message1, message2, message3]
    controllers = [331320136]  # admins list
