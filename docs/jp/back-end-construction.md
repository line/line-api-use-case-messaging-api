# バックエンドの構築手順

## 周辺リソースのデプロイ

本アプリでは以下の周辺リソースをデプロイする必要があります。

1. 共通処理レイヤー(Layer)

### 1.共通処理レイヤー(Layer)

AWS Lambda では複数 Lambda 関数で共通化して利用したい処理をレイヤーとして記述することが出来ます。
本アプリではレイヤーを利用しているので、はじめに以下の手順で、レイヤーをデプロイしてください。

- template.yaml の修正  
  backend-> Layer フォルダ内の template.yaml を開き、EnvironmentMap の dev の以下のパラメータ項目を修正する。

  - `LayerName` 任意のレイヤー名

- 以下コマンドの実行

```
cd [backend -> Layerのフォルダ]
sam build --use-container
sam deploy --guided
※プロファイル情報(default)以外を使用する場合は指定必要 sam deploy --guided --profile xxx
    Stack Name : 任意のスタック名
    AWS Region : ap-northeast-1
    Parameter Environment: dev
    #Shows you resources changes to be deployed and require a 'Y' to initiate deploy Confirm changes before deploy [Y/n]: Y
    #SAM needs permission to be able to create roles to connect to the resources in your template Allow SAM CLI IAM role creation[Y/n]: Y
    Save arguments to samconfig.toml [Y/n]: Y

    SAM configuration file [samconfig.toml]: 入力せずEnter
    SAM configuration environment [default]: 入力せずEnter

    Deploy this changeset? [y/N]: y
```

- レイヤーバージョンをメモ  
  デプロイ後、ターミナルの Outputs の項目に、レイヤー ARN とレイヤーバージョンが表示されるので、レイヤーバージョンをメモをしておく。
  レイヤーバージョンは末尾の数字の部分。  
  ※バージョンはデプロイするたびに更新されるので、初めてのデプロイの場合バージョン 1 となっているのが正しいです。
  ![コマンドプロンプトのOutput部の画像](../images/jp/out-put-description.png)

- 【確認】AWS マネジメントコンソールで Lambda のコンソールを開き、左タブから「レイヤー」を選択し、今回デプロイしたレイヤーがあることを確認する。


## アプリのデプロイ(APP)

以下の手順で、アプリ本体をデプロイしてください。

- template.yaml の修正  
  backend -> APP フォルダ内の template.yaml を開き、EnvironmentMap の dev の以下のパラメータ項目を修正する。

  - `LineChannelSecret` 【LINE チャネルの作成】で作成したMessaging API 用のチャネルのチャネルシークレット
  - `LineChannelAccessToken` 【LINE チャネルの作成】で作成したMessaging API 用のチャネルのチャネルアクセストークン
  - `RichMenuMessage` 【リッチメニューの作成】で作成した<1.send message menu>のリッチメニューID
  - `RichMenuFlex` 【リッチメニューの作成】で作成した<2.send flex-message menu>のリッチメニューID
  - `RichMenuCarousel` 【リッチメニューの作成】で作成した<3.send carousel-message menu>のリッチメニューID
  - `LayerVersion` 【1.共通処理レイヤー】の手順にてデプロイしたレイヤーのバージョン番号  
    例）LayerVersion: 1
  - `LoggerLevel` INFO or Debug  
  - `LambdaMemorySize` Lambdaのメモリサイズ  
    例）LambdaMemorySize: 128 ※特に変更する必要がない場合、最小サイズの128を指定してください。

- 以下コマンドの実行

```
cd [backend -> APP のフォルダ]
sam build --use-container
sam deploy --guided
※プロファイル情報(default)以外を使用する場合は指定必要 sam deploy --guided --profile xxx
    Stack Name : 任意のスタック名
    AWS Region : ap-northeast-1
    Parameter Environment: dev
    #Shows you resources changes to be deployed and require a 'Y' to initiate deploy Confirm changes before deploy [Y/n]: Y
    #SAM needs permission to be able to create roles to connect to the resources in your template Allow SAM CLI IAM role creation[Y/n]: Y
    ××××× may not have authorization defined, Is this okay? [y/N]: y (全てyと入力)  

    SAM configuration file [samconfig.toml]: 入力せずEnter
    SAM configuration environment [default]: 入力せずEnter

    Save arguments to samconfig.toml [Y/n]: Y
    Deploy this changeset? [y/N]: y
```

- API Gateway URLのメモ  
デプロイ成功時にOutPutにて表示されるAPI Gateway endpointのメモを取ってください。後の手順にて利用します。

## エラー対応
- デプロイ時、以下のようなエラーが出た場合、こちらの手順で解消してください。
  ```
  Export with name xxxxx is already exported by stack sam-app. Rollback requested by user.
  ```
  - backend -> Layer -> template.yamlを以下を参考に、修正後デプロイ
    ```
    Outputs:
      UseCaseLayerName:
        Description: "UseCaseLayerDev Layer Name"
        Value: !FindInMap [EnvironmentMap, !Ref Environment, LayerName]
        Export:
          Name: MessagingAPILayerDev -> こちらを任意の名称に修正
    ```
  - backend -> batch -> template.yamlを、以下の記載を参考に修正する。
    ```
    !ImportValue MessagingAPILayerDev -> MessagingAPILayerDev を先ほど入力した名称に修正
    ```
  - backend -> APP -> template.yamlを、以下の記載を参考に修正する。
    ```
    !ImportValue MessagingAPILayerDev -> MessagingAPILayerDev を先ほど入力した名称に修正
    ```

[次の頁へ](validation.md)

[目次へ戻る](../../README.md)
