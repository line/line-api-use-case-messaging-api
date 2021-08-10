# Creating a LINE channel

A channel is a communication path between a system created by a developer and the LINE Platform.
The following LINE channels are required for this app. Follow these instructions to create them.

1. LINE channel for Messaging API  
・Channel creation (Japanese only): https://developers.line.biz/ja/docs/clova-extensions-kit/create-messaging-api-channel-t4/  
・About Messaging API: https://lineapiusecase.com/en/api/msgapi.html  

## 1. Create a LINE account

*Skip this step if you already have a LINE account.

1. Download the LINE app from the download link below and create a LINE account
   https://line.me/en/

## 2. Log in to LINE Developers

LINE Developers is a site for developers to create LINE Official Accounts and LIFF apps required for this app. You can develop apps by logging in to the LINE Developers site using your LINE account.

1. Click this link and go to the login screen.
   https://developers.line.biz/en/
1. Log in with your LINE account.
1. Enter the email address and password set for your LINE account, or use the QR code login to scan the QR code from another device to log in.  
   *If you want to log in with your email address, you'll need to set it up separately in the LINE app. For more information, see:  
   https://appllio.com/line-mail-address-settings  

## 3. Create a provider

A provider is a team, company, or individual that manages multiple channels. Providers and channels have a one-to-many relationship.

1. While logged in to LINE Developers, access the LINE Developers Console.
   https://developers.line.biz/console/
2. Click the Create button next to Provider.  
   ![Creating a provider_1_ Image of the created part surrounded by a square](../images/en/line-provider-create-1-en.png)
3. Enter a provider name and click Create.
4. Confirm that the provider has been created and that your see this screen.  
   ![Creating a Provider_2](../images/en/line-provider-create-2-en.png)

## 4. Create a channel

1. Create a channel for the Messaging API
   1. On the provider screen that you just created, click Messaging API.  
      ![Create Channel_Image surrounding the Messaging API part](../images/en/line-channel-create-1-en.png)
   1. Set the items as follows:
      1. Channel type: No change
      1. Provider: No change
      1. Channel icon: No change
      1. Channel name: Any channel name
         *The channel name is the account name that will be displayed when the end user adds your account a friend. You can change it later.
      1. Channel description: Any description
      1. Large industry: Industry that matches the application content
      1. Small industry: Industry that matches the application content
      1. Email: No change
      1. Privacy Policy URL: Optional
      1. Terms of Service URL: Optional
   1. Read the LINE Official Account Terms of Service and LINE Official Account API Terms of Service, and select "I agree."
   1. Click Create to create a channel.
   1. The screen of the created channel will appear as shown in the image below, confirming that the channel creation is complete..  
      ![Creating a channel_2](../images/en/line-channel-create-2-en.png)  
      The channel secret shown in the Channel Preferences tab will be used in the following steps, so make a note of it.
   1. Go to the Messaging API tab, issue a channel access token (long-term), and make a note of it. It will be used in the following steps.

[Next page](richmenu-create.md)  

[Back to Table of Contents](README_en.md)
