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

def bulk_provision(c_iot,inputFileBucket,inputFileKey,deviceMgmtRoleArn):
    try:
        response = c_iot.create_thing_type(thingTypeName = 'smart-nursery')
        logger.info("create_thing_type: response: {}".format(response))
        
        response = c_iot.create_thing_group(thingGroupName = 'smart-nursery')
        logger.info("create_thing_group_parent: response: {}".format(response))
        
        response = c_iot.create_thing_group(thingGroupName = 'geolocation', parentGroupName = 'smart-nursery')
        logger.info("create_thing_group_child: response: {}".format(response))
        
        response = c_iot.create_thing_group(thingGroupName = 'east', parentGroupName = 'geolocation')
        logger.info("create_thing_group_child: response: {}".format(response))
        
        response = c_iot.create_thing_group(thingGroupName = 'west', parentGroupName = 'geolocation')
        logger.info("create_thing_group_child: response: {}".format(response))

        response = c_iot.create_thing_group(thingGroupName = 'demand', parentGroupName = 'smart-nursery')
        logger.info("create_thing_group_child: response: {}".format(response))
        
        response = c_iot.create_thing_group(thingGroupName = 'risk', parentGroupName = 'smart-nursery')
        logger.info("create_thing_group_child: response: {}".format(response))
        
        response = c_iot.create_thing_group(thingGroupName = 'producttype', parentGroupName = 'smart-nursery')
        logger.info("create_thing_group_child: response: {}".format(response))

        response = c_iot.create_thing_group(thingGroupName = 'utility', parentGroupName = 'producttype')
        logger.info("create_thing_group_child: response: {}".format(response))
        
        response = c_iot.create_thing_group(thingGroupName = 'security', parentGroupName = 'producttype')
        logger.info("create_thing_group_child: response: {}".format(response))
        
        response = c_iot.create_thing_group(thingGroupName = 'accessories', parentGroupName = 'producttype')
        logger.info("create_thing_group_child: response: {}".format(response))
        

        #Run the provisioning template 
        f = open("sampleTemplate.json","r")
        template = f.read()
        
        # Add atributes to the things 
        response = c_iot.start_thing_registration_task (
            templateBody = template, 
            inputFileBucket = inputFileBucket,
            inputFileKey = inputFileKey,
            roleArn = deviceMgmtRoleArn
        )

    except Exception as e:
        logger.error("create_thing: {}".format(e))

def update_index(c_iot):
    try:
        response = c_iot.update_indexing_configuration(
            thingIndexingConfiguration={
                'thingIndexingMode': 'REGISTRY_AND_SHADOW',
                'thingConnectivityIndexingMode': 'STATUS'
            },
            thingGroupIndexingConfiguration={
            'thingGroupIndexingMode': 'ON'
            }
        )
    
    except Exception as e:
        logger.error("update_index_configuration: {}".format(e))

def enable_v2logs(c_iot,loggingroleArn):
    try:
        response = c_iot.set_v2_logging_options(
            roleArn=loggingroleArn,
            defaultLogLevel='INFO',
            disableAllLogs=False
        )
        
    except Exception as e:
        raise e

# def update_shadow(c_iot,thingName):
#     try:
#         payload = {"desired":{"welcome":"aws-iot","status":"ON","brightness":"MEDIUM"},"reported":{"welcome":"aws-iot","status":"ON","brightness":"MEDIUM"}}
#         response = c_iot.update_thing_shadow(
#         thingName=thingName,
#         payload=json.dumps(payload)
#     )

    except Exception as e:
        raise e

def lambda_handler(event, context):
    logger.info("event:\n" + str(event))

    region = os.environ["AWS_REGION"]
    logger.info("region: {}".format(region))

    
    thingName = os.environ["thing_name"]
    inputFileBucket = os.environ["input_file_bucket"]
    inputFileKey = os.environ["input_file_key"]
    deviceMgmtRoleArn = os.environ["device_mgmt_role_arn"]
    loggingroleArn = os.environ["logging_role_arn"]

    c_iot = boto3.client('iot')

    #Create devices in bulk
    bulk_provision(c_iot,inputFileBucket,inputFileKey,deviceMgmtRoleArn)
    
    #Update the fleet indexing configuration
    update_index(c_iot)
    

    #Enable logging to send data to cloudwatch
    enable_v2logs(c_iot,loggingroleArn)
    
    #c_iot = boto3.client('iot-data')
    #Create shadow document for the hardware 
    #update_shadow(c_iot,thingName)
    
    #Add group associations correctly for diff things 

    return True
