# Deployment Instructions

This document provides instructions on how to deploy the chess engine web application to Heroku and AWS.

## Prerequisites

*   A free Heroku account
*   The Heroku CLI installed and authenticated
*   An AWS account
*   The AWS CLI installed and authenticated
*   Docker installed

## Deploying to Heroku

1.  **Create a Heroku app:**
    ```bash
    heroku create <your-app-name>
    ```

2.  **Set the stack to `container`:**
    ```bash
    heroku stack:set container -a <your-app-name>
    ```

3.  **Push the Docker image to Heroku:**
    ```bash
    heroku container:push web -a <your-app-name>
    ```

4.  **Release the image:**
    ```bash
    heroku container:release web -a <your-app-name>
    ```

5.  **Open the app in your browser:**
    ```bash
    heroku open -a <your-app-name>
    ```

## Deploying to AWS (using Elastic Beanstalk)

1.  **Create an Elastic Beanstalk application:**
    *   Go to the Elastic Beanstalk console and create a new application.
    *   Choose a name for your application and a domain.
    *   For the platform, select "Docker" and for the platform branch, select "Docker running on 64bit Amazon Linux 2".
    *   For the application code, select "Upload your code" and upload the `source.zip` file (you will need to create this file by zipping the contents of the repository).

2.  **Configure the environment:**
    *   Once the environment is created, go to the "Configuration" page.
    *   In the "Software" category, click "Edit".
    *   For the "Container options", set the "Port" to `5000`.

3.  **Deploy the application:**
    *   Click "Apply" to save the changes.
    *   Elastic Beanstalk will now deploy your application. You can monitor the progress in the "Events" page.

4.  **View the application:**
    *   Once the deployment is complete, you can click the URL at the top of the page to view your application.
