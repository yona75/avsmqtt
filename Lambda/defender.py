#
# lambda function for security , device defender 
#

#required libraries
import boto3
import logging
import os

# configure logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def update_audit_settings(c_iot,serviceroleArn,snsArn,deviceDefenderRole):
    try: 
        response = c_iot.update_account_audit_configuration(
            roleArn=serviceroleArn,
            auditNotificationTargetConfigurations={
                'SNS': {
                    'targetArn': snsArn,
                    'roleArn': deviceDefenderRole,
                    'enabled': True
                }
            },
            auditCheckConfigurations={
                'IOT_POLICY_OVERLY_PERMISSIVE_CHECK': {
                'enabled': True
                }
            }
        )
        
        logger.info("update_audit_settings: response: {}".format(response))


    except Exception as e:
        logger.error("update_audit_settings: {}".format(e))

    
def lambda_handler(event, context):
    logger.info("event:\n" + str(event))

    region = os.environ["AWS_REGION"]
    logger.info("region: {}".format(region))
    
    serviceroleArn = os.environ["defender_service_role_arn"]
    snsArn = os.environ["sns_arn"]
    deviceDefenderRole = os.environ["device_defender_role_arn"]

    c_iot = boto3.client('iot')

    #Update audit settings 
    update_audit_settings(c_iot,serviceroleArn,snsArn,deviceDefenderRole)
    
    
    return True
