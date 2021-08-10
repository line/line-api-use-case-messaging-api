# リッチメニューの設定

本アプリで使用するリッチメニューはMessagingAPIのリッチメニューを作成用APIを使用します。また、より簡単に設定いただけるようPostmanを使用した手順を説明します。その他の詳細は以下を参照ください。

リッチメニューの仕様： https://developers.line.biz/ja/docs/messaging-api/using-rich-menus/  
リッチメニューのAPI： https://developers.line.biz/ja/reference/messaging-api/#rich-menu  

## Postmanのインストール
リッチメニュー作成の手順では、Postmanを利用します。  
本手順に従ってリッチメニューを導入する場合、以下URLから自身の環境に合ったものをインストールしてください。
https://www.postman.com/downloads/

## リッチメニューの設定
1. リッチメニューの作成
   1. Postmanを起動する
   1. Importから、richmenu_setting -> フォルダ内の rich menu.postman_collection.jsonを開く  
   ![postman_import](../images/jp/postman_import.png)
   1. <1.send message menu>のHeaders/AuthorizationのValueの{channel access token}に【Messaging API 用のチャネルを作成】で発行したチャネルの長期アクセストークンを入力してファイルを上書き保存する
   ※このとき、Bearerと{channel access token}の間には半角スペースを入れてください
   1. Sendを押下するとResponseよりリッチメニューIDを確認できるので、控えておく  
   ![send_richmenu](../images/jp/send_richmenu.png)
   1. <2.send flex-message menu>と<3.send carousel-message menu>についても3,4の手順に従い、リッチメニューIDを発行する
1. リッチメニューの画像を設定する
   1. <4.link richmenu and image>のHeaders/AuthorizationのValueの{channel access token}に【Messaging API 用のチャネルを作成】で発行したチャネルの長期アクセストークンを入力してファイルを上書き保存する
   ※このとき、Bearerと{channel access token}の間には半角スペースを入れてください
   1. <4.link richmenu and image>のURLの{1,2,3で返却されたrichmenuid}に、<1.send message menu>にて返却されたrichmenuIDを入力して、ファイルを上書き保存する
   1. Bodyタブにて、binaryを選択し、selectFileにて、ricimenu_setting -> menu_imgフォルダ のmessage_ja.pngを選択する。  
   ![richmenu-image-link](../images/jp/richmenu-image-link.png)
   1. Sendを押下し、Responseで {} と返ってきていることを確認する。  
   ※{} 以外の場合間違いがあるので、誤りがないか確認し、再度試してください。
   1. 以上の手順を、<2.send flex-message menu>と<3.send carousel-message menu>にて発行されたrichmenuIDに対しても行う。なお、画像は<2.send flex-message menu>のrichmenuIDのとき、flex_ja.pngを選択し、<3.send carousel-message menu>のrichmenuIDのとき、carousel_ja.pngを選択する。


[次の頁へ](back-end-construction.md)

[目次へ戻る](../../README.md)
