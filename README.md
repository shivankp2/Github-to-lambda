# Github-to-lambda
**Target : To schedule a lambda functiopn which runs in every 24 hours and fetch the daily news from Tesla from past 1 day.**

As per the architecture diagram from below we are making changes in lambda function at local and commiting it. The codebuild works here which builds the dependecies and functions together in a zip file and deploy it to then lambda function.

![arch  diagram ](https://user-images.githubusercontent.com/36138430/170344886-ba56db4e-825f-44a5-bd18-3da7b8e91bea.jpg)

**Process** :
1.**create a lambda function from console** : 

  1.1 : Sign in to the [Lambda console](https://console.aws.amazon.com/lambda).

  1.2 : Choose Create function.

  1.3 : For Function name, enter "name of your choice".

  1.4 : Choose Create function.
  
 The example function returns a 200 response to clients, and the text Hello from Lambda!.

The default Lambda function code should look similar to the following:

````````
exports.handler = async (event) => {
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
    return response;
};

````````

2.  Create a codeBuild proect and attach github push trigger to it: [CodeBuild](https://console.aws.amazon.com/codesuite/codebuild/project/new).

![codebuild](https://user-images.githubusercontent.com/36138430/170345073-8e8fa181-d04a-4221-b436-93d2a4a855a2.png)

3. Edit the lambda.py file and make your changes.

![code](https://user-images.githubusercontent.com/36138430/170345364-2e88dd2d-b8c5-4adb-af1b-590ce8ccac39.png)

5. commit the changes to main branch and push the changes.
6. After the changes are being pushed code build will work and build and deploy the changes to lambda function.

![codebuildchanegs](https://user-images.githubusercontent.com/36138430/170345517-c7c60005-fff0-47c7-a5c4-3d0a4827e45f.png)


**Note : Checked manually and it is working fine we are able to fetch the news details from the newsapi.org**.

![lambdaresult](https://user-images.githubusercontent.com/36138430/170345809-cfb450ee-57f7-4d8d-9db8-dff33857ff80.png)

To schedule the event so that it will automatically triggered in 24 hours we enabled a eventbridge which scheduled the lambda fucntion to fetch the details from newsapi.org

**To create CloudWatch Event - Rule - to schedule Lambda function invocation**.
Go to [Cloudwatch console](https://console.aws.amazon.com/cloudwatch/home).

Go to Event -> Rules

Create Rule

find the below screenshot to check more.

![event](https://user-images.githubusercontent.com/36138430/170347091-f9775693-7796-45d2-9b67-b42e01435c81.png)

![event1](https://user-images.githubusercontent.com/36138430/170347063-82672a97-3154-46cc-99ac-8feb35727f3a.png)
