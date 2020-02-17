#
# lambda function for bulk provisioning , fleet indexing and logging 
#

#required libraries
import boto3
import logging
import os
import json

# configure logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def update_shadow(c_iot,thingName):
    try:
        payload = {"state" : {"desired":{"welcome":"aws-iot","status":"ON","brightness":"MEDIUM"},"reported":{"welcome":"aws-iot","status":"ON","brightness":"MEDIUM"}}}
        
        response = c_iot.update_thing_shadow(
            thingName=thingName,
            payload=json.dumps(payload)
        )

        logger.info("update_shadow_complete: response: {}".format(response))

    except Exception as e:
        raise e

def lambda_handler(event, context):
    logger.info("event:\n" + str(event))
    
    # if event['RequestType'] == 'Delete':
    #     send(event, context, SUCCESS)
    #     return

    thingName = os.environ["thing_name"]
    c_iot = boto3.client('iot-data')
    
    #Create shadow document for the hardware 
    update_shadow(c_iot,thingName)  

    # send(event, context, SUCCESS)
    
    return True