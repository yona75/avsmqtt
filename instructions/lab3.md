![alt text](../images/aws_logo.png)

# Lab 3 : Command and Control Alexa enabled IoT device(s)

In this lab, you will learn how to perform command and control on Alexa enabled IoT devices. You will create a custom  skill and a lambda function that will interact with the device state (shadow) in AWS IoT Core. At the end of this lab, you will be able to turn the device led on / off using voice commands. 

## <span style="color:orange"> You will build step 1b of this architecture : </span>
![alt text](../images/arch-1b.png)

## A. Configure Lambda functions for interacting with Alexa skills

##### Please login to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/) and select *Applications* (on the left pane) -> reinventavsmqtt* application. ###

![alt text](../images/lambdahome.png)

1.  Under Resources section, please select the Lambda function with Logical ID   *"DeviceShadowLambda"* 

    ![alt text](../images/shadow.png)

2. Click the *Select a test event dropdown* (top right corner) -> Choose Configure test events. 

    ![alt text](../images/lambdatest.png)

    -   A window will appear, keep everything default, put the **Event name** as **test** , click **Create** button
    -  This will configure the test event and bring you back to the lambda console 

3. Click on *Test* (top right corner) , check if the *Execution Result* is a success 
    - If it fails, check the logs to identify the problem. Ask support staff for help if you need. 

<span style="color:lightgreen">If step 3 is a success, proceed to validate if the shadow is updated for the thing.</span>

##### Please navigate to the [AWS IoT Console](https://console.aws.amazon.com/iot/) and select *Manage* (on the left pane) -> *Things* ### 

4. On the right pane , you will see the  *NxP* device 

    ![alt text](../images/nxp.png) 

5. Please click on it and choose Shadow (on the left). You will see the status of the device here :

    ![alt text](../images/nxpshadow.png) 

##### Please navigate back to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/) and select *Applications* (on the left pane) -> reinventavsmqtt* application. ###

6. Under Resources section, please select the Lambda function with Logical ID *"AlexaSkillProcessorLambda"* 
    - Check *"Alexa Skills Kit"* is added as a trigger
    - Copy the ARN of this lambda from the top left corner and paste it in a local notepad. 

    ![alt text](../images/lambdaarn.png) 

    <span style="color:orange">We will use this when configuring the Alexa endpoint later in this lab. </span>

## B. Create Alexa skill   

Log into the [Alexa developer console](https://developer.amazon.com/alexa/console/ask?) with your Amazon Developer account. 

1. Create Skill

    ![alt text](../images/buildingaskill.png)

    Click Create Skill on the right-hand side of the console. A new page displays.

    - Skill name - *nursery*
    - Default language - *English (US)*
    - Choose a model to add to your skill -  *Custom*
    - Choose a method to host your skill's backend resources -  *Provision your own*
    - Click on Create Skill button on the top right corner.

2. Choose a template
   
    Choose "Start from scratch" and click on "Choose" button on the top right corner.

     ![alt text](../images/template.png)

3. Create Interaction Schema

    - Open the [Skill Schema definition](../templates/skills.json) json file.
    - On the left pane, click on "JSON Editor" option from the "Interaction Model" section.
    - Copy the contents of the skill.json file and click on "Save Model".

     ![alt text](../images/json.png)

4. Configure the Endpoint

    - On the left Pane, click on "Endpoint" section.
    - Choose "AWS Lambda ARN" option.
    - Paste the "AlexaSkillProcessorLambda" lambda ARN copied in Section A - step 6.
    - Click on "Save Endpoints".

     ![alt text](../images/endpoint.png)

5. Build Model

    - Click on the "Invocation" option from the "Interaction Model" section.
    - Click "Save Model".
    - Click "Build Model".
    
    ![alt text](../images/build.png)

## C. Test the custom Alexa skill  

6. <span style="color:orange">Test the Skill from the Simulator</span>

   - Navigate to the "Test" section on the header.
   
   - When there is a pop-up asking for Microphone access, please select "Allow".
   
   - Change the "Test is disabled for this skill" to "development".

       ![alt text](../images/test.png)
   
   - On the left pane, try the below commands.
        - *"Ask re invent swing status"*
            - this should return the state of the shadow of your nxp device.
        - *"Ask re invent set swing speed LOW"*
            - this should update the desired state of the crib speed to "LOW".

8. <span style="color:orange">Test the skill from the NxP Hardware now</span>

    - Unmute the microphone on the kit (press SW1) if muted
        - red led on the board indicates the microphone is muted
    
        ![alt text](../images/board1.png)
    
    - Try the below commands  

        - say *"Alexa open re invent"*

        - *"crib status"*
            - this should return the state of your nxp device.

        - say *"Alexa open re invent"*

        - *"set crib speed HIGH"*
            - this should update the desired state of the crib speed to "HIGH".


Congratulations! You now have configured your hardware device to interact with custom Alexa skills. You have also used IoT shadow to change the status of your device using voice commands. 

### See you in [lab4](./lab4.md). 
