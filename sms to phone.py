import time
from time import sleep 
from sinchsms import SinchSMS

def sendSMS():
    number="your mobile number"
    app_key="your app key"
    app_secret="your app secret"

    message="Hello Message!!!"
    client = SinchSMS(app_key,app_secret)
    print("Sending '%s' to %s" % (message, number))

    response = client.send_message(number, message)
    message_id = response['messageId']
    response = client.check_status(message_id)

    while response['status'] != 'Successful':
        print(response['status'])
        time.sleep(1)
        response = client.check_status(message_id)
    
    print(response['status'])
if __name__ == "__main__":
    sendSMS()