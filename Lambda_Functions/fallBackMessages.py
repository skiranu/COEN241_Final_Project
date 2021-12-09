import json

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def fallBack_handler(event, context):

    """logger.info('## Tanvi EVENT')

    logger.info(event['recentIntentSummaryView'])
    logger.info(event['recentIntentSummaryView'][0]['slots'])"""

    logger.info(event)

    intent = event['recentIntentSummaryView'][0]['intentName']
    slot = event['recentIntentSummaryView'][0]['slots']
    slotNameDept = event['recentIntentSummaryView'][0]['slots']['departmentName']
    slotNameQuart = event['recentIntentSummaryView'][0]['slots']['quarter']
    slotNameGrad = event['recentIntentSummaryView'][0]['slots']['gradOrUndergrad']

    response = ""

    if(intent == "StudentDetails"):
        if(slotNameGrad is None):
            # if(slot["departmentName"] is None):
            response = "Sorry, I did not understand. Possible values are Gradute / Undergraduate."
            return {
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Fulfilled",
                    "message": {
                        "contentType": "PlainText",
                        "content": response
                    }
                }
            }
        elif(slotNameDept is None):
            response =  response = "Sorry, I did not understand. Possible values are CS/ MECH / ECE / MBA."
            return {
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Fulfilled",
                    "message": {
                        "contentType": "PlainText",
                        "content": response
                    }
                }
            }

        elif(slotNameQuart is None):
            # if(slot["quarter"] is None):
            response = "Sorry, I did not understand. Possible values are Winter / Spring / Summer / Fall."
            return {
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Fulfilled",
                    "message": {
                        "contentType": "PlainText",
                        "content": response
                    }
                }
            }

    elif(intent == "Greetings"):
        if(slot['Name'] is None):
            response = "Sorry, I did not understand. I would love to know your name!"
    # else:
    #     response = """Sorry, I did not understand. Most common topics students need help with are:
    #             \n1. Application Deadline\n2. Visa\n3.Course Fee\n4.Covid Information"""


    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": response
            }
        }
    }


