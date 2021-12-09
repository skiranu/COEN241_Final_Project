import json

def visaInfo_handler(event, context):
    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": "For Visa and/or immigration related information, please visit https://www.scu.edu/globalengagement/international-students/apply-and-getting-started/immigration-process/ . You can also drop an email to iss@scu.edu. Is there anything else I can help you with today?"
            }
        }
    }
