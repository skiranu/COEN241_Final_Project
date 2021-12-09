import json
import os




def lambda_handler(event,context):

    '''get the values of the slots, use your slot names at the end'''
    name = event["currentIntent"]["slots"]
    gradOrUndergrad = name["gradOrUndergrad"]
    department = name["departmentName"]
    quarter = name["quarter"]

    print(gradOrUndergrad, department, quarter)

    event["sessionAttributes"] = gradOrUndergrad
    event["sessionAttributes"] = department
    event["sessionAttributes"] = quarter


    response ={
        "sessionAttributes":{
            "gradOrUndergrad":gradOrUndergrad,
            "departmentName": department,
            "quarter": quarter
        },

        "dialogAction":
            {
                "fulfillmentState":"Fulfilled",
                "type":"Close",
                "message":
                    {
                        "contentType":"PlainText",
                        "content": "Thank you for providing me the details. How can I help you?"
                    }
            }
    }
    return response