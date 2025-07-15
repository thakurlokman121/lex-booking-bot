# lex-booking-bot
# 🧠 Lex + Lambda Hotel Booking Bot (Voice Bot Demo)

## 📦 Overview
A modular Python Lambda function designed to process hotel bookings through an Amazon Lex bot. The architecture supports slot validation, DynamoDB queries, and voice-based interactions via Amazon Connect.

## 🚀 Key Features
- Multi-turn conversations using Lex slots
- Validation logic with Python (`datetime`, `re`)
- Booking persistence via DynamoDB
- Lex-compatible structured responses
- Modular submodules: validation, storage, formatting

## 🗂️ File Structure
- `main.py` – Lambda entry point for Lex
- `validation.py` – Validates slots (date, guests)
- `dynamo.py` – Queries/saves bookings to DynamoDB
- `response_builder.py` – Formats Lex response payloads
- `constants.py` – Centralized values (bot name, default city)
- `__init__.py` – Exposes functions for import

## 🧰 AWS Resources
- Lambda Function: `HotelBookingLambda`
- DynamoDB Table: `HotelBookings`
- IAM Role: `LexBookingLambdaRole`
- Lex V2 Bot: `BookingAssistantBot`
- Amazon Connect Flow: `BookingFlow`

## 📦 Packaging & Deployment
To deploy this code to AWS Lambda:
1. Navigate to `lex_booking_bot/`  
2. Run:
   ```bash
   zip -r ../lambda_package.zip .
