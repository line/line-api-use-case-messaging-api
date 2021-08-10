# Rich menu settings

The rich menu used in this application uses the API for creating the Messaging API's rich menu. We'll also walk you through the steps using Postman to make it easier to set up. See below for other details.  

Rich Menu specs: https://developers.line.biz/en/docs/messaging-api/using-rich-menus/  
Rich Menu API: https://developers.line.biz/en/reference/messaging-api/#rich-menu

## Install Postman

In the procedure for creating a rich menu, we will use Postman.  
If you want to install the rich menu according to this procedure, install the one that suits your environment from this URL.  
https://www.postman.com/downloads/

## Rich menu settings

1. Creating a Rich Menu
   1. Start Postman
   1. From Import, open richmenu_setting > rich menu.postman_collection.json folder  
   ![postman_import](../images/en/postman_import-en.png)
   1. Enter the long-term access token for the channel issued in [Create a channel for the Messaging API] in the {channel access token} field of the Headers/Authorization value in the <1. send message menu> and save the file by overwriting
   At this time, please put a space between Bearer and {channel access token}
   1. Press "Send" to confirm the Rich Menu ID from Response, and write it down  
   ![send_richmenu](../images/en/send_richmenu-en.png)
   1. For <2.send flex-message menu> and <3.send carousel-message menu>, follow steps 3 and 4 to issue a rich menu ID
1. Set the image for the rich menu
   1. Enter the long-term access token for the channel issued in [Create a channel for the Messaging API] in the {channel access token} field of the Headers/Authorization value in the <4. link richmenu and image> and save the file by overwriting
   At this time, please put a space between Bearer and {channel access token}
   1. In the URL of <4.link richmenu and image>, enter the richmenuID returned by <1. send message menu> in the {richmenuid returned by 1,2,3} field and overwrite the file
   1. In the Body tab, select binary, and in selectFile, select message_ja.png in the richmenu_setting > menu_img folder  
   ![richmenu-image-link](../images/en/richmenu-image-link-en.png)
   1. Click Send and make sure that {} is returned in Response  
   *If the response is other than {}, there is an error. Please check and try again
   1. The above steps are also performed for the richmenu IDs issued in <2. send flex-message menu> and <3. send carousel-message menu>. For the image, select flex_en.png for the richmenuID of <2.send flex-message menu> and select carousel_en.png for the richmenuID of <3.send carousel-message menu>.


[Next page](back-end-construction.md)  

[Back to Table of Contents](README_en.md)
