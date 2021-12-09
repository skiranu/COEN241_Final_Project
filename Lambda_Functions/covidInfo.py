import json

def lambda_handler(event, context):
    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": "Please visit https://www.scu.edu/preparedscu/ to view SCU's covid guidelines and you can also visit https://www.nytimes.com/interactive/2021/us/santa-clara-california-covid-cases.html to view current covid activity in Santa Clara county. Is there anything else I can help you with today?"
            }
        }
    }
