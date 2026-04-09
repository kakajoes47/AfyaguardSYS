import os
import africastalking

def send_alert(message):
    USERNAME=os.getenv("AT_USERNAME")
    API_KEY=os.getenv("AT_API_KEY")
    PHONE=os.getenv("AT_PHONE")

    if not USERNAME or not API_KEY or not PHONE:
        print("Missing SMS credentials")
        return

    try:
        africastalking.initialize(USERNAME,API_KEY)
        africastalking.SMS.send(message,[PHONE])
        print("SMS sent")
    except Exception as e:
        print("SMS error:",e)
