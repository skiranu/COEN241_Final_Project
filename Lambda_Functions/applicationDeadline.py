import json
import os
import boto3
import csv


def lambda_handler(event,context):
    s3_resource = boto3.resource('s3')
    s3_object = s3_resource.Object("coen241studenthelperchatbot", "chatbot.csv")
    data = s3_object.get()['Body'].read().decode('utf-8').splitlines()

    res=''
    lines = csv.reader(data)
    headers = next(lines)
    '''print('headers: %s' %(headers))'''
    intent_name = event["currentIntent"]["name"]

    dept = event["sessionAttributes"]['departmentName']
    dept = dept.upper()
    quarter = event["sessionAttributes"]['quarter']
    quarter = quarter.capitalize()
    gradOrUgr = event['sessionAttributes']['gradOrUndergrad']
    gradOrUgr = gradOrUgr.upper()
    if intent_name == 'TopicApplicationDeadline':
        for line in lines:
            #print complete line
            #print index wise
            if line[0] == dept and line[2] == quarter and line[3] == gradOrUgr:
                res =line[1]

    print(intent_name,res)
    dept = event["sessionAttributes"]['departmentName']
    quarter = event["sessionAttributes"]['quarter']
    gradOrUgr = event['sessionAttributes']['gradOrUndergrad']
    response ={
        "sessionAttributes":{
            "key1":"value1",
            "key2":"value2",
            "key3":"value3"

        },
        "dialogAction":
            {
                "fulfillmentState":"Fulfilled",
                "type":"Close",
                "message":
                    {
                        "contentType":"PlainText",
                        "content": "The deadline for "+dept+" department for "+quarter+" quarter is: "  +res+". Is there anything else I can help you with today?"
                    }
            }
    }
    return response


