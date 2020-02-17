# Frequently Asked Questions 

1. **How do I login to AWS Console ?**
    -   Launch [Team Dashboard](https://dashboard.eventengine.run/dashboard)
    - Paste the 12 digit Hash key provided to you by AWS 
    - Click Accept Terms & Login
    - Click AWS Console 
    - Open AWS Console

    ![alt text](../images/account.png) 

2. Where do I get the AWS Account # ? 
    - Launch [Team Dashboard](https://dashboard.eventengine.run/dashboard)
    - AWS Account # is the Team name (screenshot above)

3. Where do I get the Device Serial # ? 
    - Please navigate to the [AWS IoT Console](https://console.aws.amazon.com/iot/) 
    - select Manage -> Things 
        - Thing Name is device serial #

    ![alt text](../images/thing.png)

4. How do I connect the hardware to my laptop ? 
    - Connect both the usb ports 
    - Ask for an USB extender from AWS if donot have 2 ports
    
    ![alt text](../images/laptop.jpg)

5. How do I login to the hardware kit ? 
    -   Mac -  [screen](./serial.md)
    -   Windows - [putty](./serial.md)
    -   Linux -  [screen / minicom](./serial.md)

6. How do I check the logs on the kit ? 

    - Run the below on the serial console : 
    ```
      enable_usb_log
      logs
    ```

7. How do I exit the serial console ? 
    - type CTRL-A and then CTRL-K and then yes 

8. I have setup all the commands, why Alexa is still not talking to me ? 
    
    - Check the logs on the serial console (follow step 6 above). 

    - Try power recycling the device, if log output is static
        
9. LWA Registration shows successful on the webpage, but   devices still dont respond ?
    - Check the Account ID is linked correctly on the AVS Product page 

        ![alt text](../images/avs3.png)

    - If its correct, please re-run the serial commands in lab 2 , ensure there is no typo 

    - Power recycle the device and complete the LWA registration again 

10. Post LWA registration, why I am getting SSL errors on the logs ? 

    - Please re-run the serial commands in lab 2 , ensure there is no typo 

    - Power recycle the device and complete the LWA registration again 

11. Alexa is not responding or taking long to respond , after successful registration ? 

    - Please check if there is a blinking red icon , that implies network connectivity issues
    - Wait for sometime and power recycle the device if required 
    - If still not resolved, ask AWS support staff for help 

