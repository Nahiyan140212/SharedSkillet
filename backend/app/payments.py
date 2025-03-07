import stripe
import os

stripe.api_key = os.environ.get("STRIPE_API_KEY")

def process_payment(amount: float, token: str):
    payment_intent = stripe.PaymentIntent.create(
        amount=int(amount * 100),
        currency="usd",
        payment_method=token,
        confirmation_method="manual",
        confirm=True
    )
    return payment_intent["id"]