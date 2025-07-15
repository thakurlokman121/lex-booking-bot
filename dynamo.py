import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('HotelBookings')

def check_existing_booking(city, check_in_date):
    response = table.get_item(Key={'City': city, 'CheckInDate': check_in_date})
    return response.get('Item')

def save_booking(city, check_in_date, guests):
    table.put_item(Item={
        'City': city,
        'CheckInDate': check_in_date,
        'Guests': guests
    })
