def build_validation_response(slot_to_elicit, message):
    return {
        'sessionState': {
            'dialogAction': {'type': 'ElicitSlot', 'slotToElicit': slot_to_elicit}
        },
        'messages': [{
            'contentType': 'PlainText',
            'content': message
        }]
    }

def build_fulfillment_response(session_attrs, message):
    return {
        'sessionState': {
            'dialogAction': {'type': 'Close', 'fulfillmentState': 'Fulfilled'},
            'sessionAttributes': session_attrs
        },
        'messages': [{
            'contentType': 'PlainText',
            'content': message
        }]
    }
