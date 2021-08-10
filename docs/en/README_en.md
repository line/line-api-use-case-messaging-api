# Overview

This is the demo app source code for the [Messaging API](https://lineapiusecase.com/en/api/msgapi.html) provided on the [LINE API Use Case site](https://lineapiusecase.com/en/top.html). By referring to the steps described in this article, you can develop an app that uses Messaging API.

Messaging API is an API that allows you to communicate with LINE users through the LINE Official Account you prepared. By using the Messaging API, you can offer your services in LINE chat rooms.

The source code environment introduced on this page uses AWS.

※ [日本語ドキュメントはこちらからご確認いただけます。](../../README.md)

# Libraries

## Python

Install Python version 3.8 or later if it isn't already installed.

You can check if it's installed by entering this command in Command Prompt or Terminal:

```
python --version
```

If Python is installed, the version will be returned. For example:

```
Python 3.8.3
```

Install Python (3.8 or higher), used for back-end development, in your local development environment if it's not already installed.

Python installation reference site:

Windows: https://docs.python.org/3/using/windows.html  
Mac: https://docs.python.org/3/using/mac.html

## AWS SAM

The AWS Serverless Application Model (AWS SAM) is used to deploy this app.

See the [official AWS documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) to register and set up an AWS account, and install the AWS SAM CLI and Docker.  

*Recommended version of SAM CLI is 1.15.0 or later.  
*Docker installation is also required, with or without local testing.

### Reference points in the official documentation

Complete these items in the official documentation and proceed to the next step. If you have already installed it, you can skip this section.

*This document was created in December 2020 and may be inconsistent with the latest official documentation.

1. Install AWS SAM CLI
1. Set up AWS authentication credentials
1. (Optional) Tutorial: Deploying the Hello World app

# Getting Started / Tutorial

This procedure explains how to create a LINE channel, build the backend and frontend, and check the operation, which are necessary for app development.

See these steps to build your local and production (AWS) environment:

- **[Create a LINE channel](liff-channel-create.md)**
- **[Create a rich menu](richmenu-create.md)**
- **[Build the back-end](back-end-construction.md)**
***
- **[Check operation](validation.md)**
***

# License

All files on Messaging API are free to use without conditions.

Download and clone to start developing apps using LINE API.

See [LICENSE](LICENSE) for details. (English)

# How to contribute

Thank you for taking the time to contribute. LINE API Use Case Messaging API isn't different from any other open source projects. You can help by:

- Filing an issue in [the issue tracker](https://github.com/line/line-api-use-case-messaging-api/issues) to report bugs and propose new features and improvements.
- Asking a question using [the issue tracker](https://github.com/line/line-api-use-case-messaging-api/issues).
- Contributing your work by submitting [a pull request](https://github.com/line/line-api-use-case-messaging-api/pulls).

When you are sending a pull request, be aware of and accepting the following:

- Grant [the same license](LICENSE) to the contribution
- Represent the contribution is your own creation
- Not expected to give support for your contribution
