from nltk.chat.util import Chat, reflections
from .models import Appointment  # Import your model if using Django ORM

# Define pairs for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, Please provide your Email."]
    ],
    [
        r"I want to book an appointment",
        ["Sure, which specialization are you looking for? We have Cardiology, Dermatology, Orthopedics, Pediatrics, and more."]
    ],
    [
        r"I need a (.*) appointment",
        ["Great! You have selected %1. When would you like to schedule your appointment?"]
    ],
    [
        r"book appointment on (.*) for (.*)",
        ["Your appointment for %2 on %1 has been booked. "]
    ],
    [
        r"My name is (.*)",
        ["Thanks, %1. Please provide your contact number."]
    ],
    [
        r"My contact number is (.*)",
        ["Thanks for providing your contact number: %1. Please provide your email address."]
    ],
    [
        r"My email is (.*)",
        ["Your email %1 has been recorded. We will send all details to this address."]
    ],
    [
        r"thank you",
        ["You're welcome! Have a great day!"]
    ]
]

# Create chatbot
appointment_chatbot = Chat(pairs, reflections)

def chatbot_response(user_input, user_data):
    response = appointment_chatbot.respond(user_input)

    # Process and store the appointment details if booking is confirmed
    if "Your appointment for" in response:
        specialization = user_data.get('specialization')
        date = user_data.get('date')
        contact_number = user_data.get('contact_number')
        email = user_data.get('email')
        name = user_data.get('name')

        if specialization and date and contact_number and email and name:
            Appointment.objects.create(
                specialization=specialization,
                date=date,
                contact_number=contact_number,
                email=email,
                name=name
            )

    return response
