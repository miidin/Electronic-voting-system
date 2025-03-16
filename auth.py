import random
from flask import jsonify
from twilio.rest import Client

# Twilio Credentials (Replace with your Twilio details)
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+your_twilio_number"

otp_storage = {}  # Temporary storage for OTPs

def send_otp(phone):
    otp = random.randint(100000, 999999)
    otp_storage[phone] = otp  # Store OTP

    # Send OTP via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=f"Your Secure Voting OTP is: {otp}",
        from_=TWILIO_PHONE_NUMBER,
        to=phone
    )
    
    return jsonify({"message": "OTP sent successfully!"})

def verify_otp(otp):
    for phone, stored_otp in otp_storage.items():
        if int(otp) == stored_otp:
            return jsonify({"success": True})  # OTP is correct

    return jsonify({"success": False})  # OTP is incorrect
