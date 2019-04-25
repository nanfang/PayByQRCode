from common.constants import MESSAGE_GROUP


def get_message_group(current_customer):
    return MESSAGE_GROUP % current_customer.replace(' ', '_')
