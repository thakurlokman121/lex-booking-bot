from lex_booking_bot import (
    validate_date,
    validate_guest_count,
    check_existing_booking,
    save_booking,
    build_validation_response,
    build_fulfillment_response,
    BOT_NAME
)

def lambda_handler(event, context):
    slots = event['sessionState']['intent']['slots']
    session_attrs = event['sessionState'].get('sessionAttributes', {})
    
    city = slots['City']['value']['interpretedValue']
    check_in = slots['CheckInDate']['value']['interpretedValue']
    guests = slots['Guests']['value']['interpretedValue']

    if event['invocationSource'] == 'DialogCodeHook':
        if not validate_date(check_in):
            return build_validation_response("CheckInDate", "Please enter a valid date (YYYY-MM-DD).")
        if not validate_guest_count(guests):
            return build_validation_response("Guests", "Guest count must be a positive number.")
        return { 'sessionState': { 'dialogAction': { 'type': 'Delegate' } } }

    if check_existing_booking(city, check_in):
        message = f"A booking already exists for {city} on {check_in}."
    else:
        save_booking(city, check_in, guests)
        message = f"{BOT_NAME}: Hotel booked in {city} for {guests} guest(s) on {check_in}."

    return build_fulfillment_response(session_attrs, message)
