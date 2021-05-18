import os
import sys
import json
import logging
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, PostbackEvent, FollowEvent, TextMessage, ImageMessage,
    TextSendMessage, FlexSendMessage, QuickReply, TemplateSendMessage,
    ConfirmTemplate, ButtonsTemplate
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from common import (common_const, utils)


# ログ出力設定
LOGGER_LEVEL = os.environ.get("LOGGER_LEVEL")
logger = logging.getLogger()
if LOGGER_LEVEL == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    logger.error('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    logger.error('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


def get_sigunature(key_search_dict):
    """
    署名発行に必要なx-line-signatureを大文字小文字区別せずに取得し、署名内容を返却する

    Parameters
    ----------
    key_search_dict : dict
        Webhookへのリクエストのheaders

    Returns
    -------
    signature : str
        LINE Botの署名
    """
    for key in key_search_dict.keys():
        if key.lower() == 'x-line-signature':
            signature = key_search_dict[key]
            return signature


def convert_user_id(event):
    """
    LINE UserIdのマスク処理

    Parameters
    ----------
    event : dict
        Webhookへのリクエスト内容。

    Returns
    -------
    log_event : dict
        UserIdマスク後のリクエスト内容。
    """
    log_body = json.loads(event['body'])
    update_body = []
    for linebot_event in log_body['events']:
        linebot_event['source']['userId'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        update_body.append(linebot_event)
    del log_body['events']
    log_body['events'] = update_body
    log_event = event
    log_event['body'] = json.dumps(log_body, ensure_ascii=False)

    return log_event


def lambda_handler(event, context):
    """
    Webhookに送信されたLINEトーク内容を返却する

    Parameters
    ----------
    event : dict
        Webhookへのリクエスト内容。
    context : dict
        コンテキスト内容。

    Returns
    -------
    Response : dict
        Webhookへのレスポンス内容。
    """
    log_event = event.copy()
    logger.info(convert_user_id(log_event))
    signature = get_sigunature(event['headers'])
    body = event['body']
    error_json = utils.create_error_response('Error')
    error_json['isBase64Encoded'] = False

    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        logger.error('Got exception from LINE Messaging API: %s\n' % e.message)
        for m in e.error.details:
            logger.error('  %s: %s' % (m.property, m.message))
        return error_json
    except InvalidSignatureError as e:
        logger.error('Got exception from LINE Messaging API: %s\n' % e.message)
        return error_json
    else:
        ok_json = utils.create_success_response(
            json.dumps('Success'))
        ok_json['isBase64Encoded'] = False
        return ok_json

    # データを貯めるなどの処理を実施したい場合は、SQSなどにメッセージ通知をして、それをトリガーに別途Lambdaを起動して処理する


@handler.add(MessageEvent, message=TextMessage)
def text_message(line_event):
    """
    Webhookに送信されたLINEメッセージ(テキスト)イベントについて処理を実施する

    Parameters
    ----------
    line_event : dict
        LINEメッセージイベント内容。

    """
    text = line_event.message.text
    line_bot_api.reply_message(
        line_event.reply_token,
        TextSendMessage(text=text))


@handler.add(MessageEvent, message=ImageMessage)
def image_message(line_event):
    """
    Webhookに送信されたLINEメッセージイベント(画像)について処理を実施する

    Parameters
    ----------
    line_event: dict
        LINEメッセージイベント内容。

    """
    line_bot_api.reply_message(
        line_event.reply_token,
        TextSendMessage(text='画像を受け付けました(画像は保存されません)'))


@handler.add(PostbackEvent)
def postback(line_event):
    """
    Webhookに送信されたLINEポストバックイベントについて処理を実施する

    Parameters
    ----------
    line_event: dict
        LINEメッセージイベント内容。

    """
    param_list = line_event.postback.data.split('&')
    action = None
    action_type = None
    for param in param_list:
        if param.split('=')[0] == 'action':
            action = param.split('=')[1]
        elif param.split('=')[0] == 'lang':
            language = param.split('=')[1]
        else:
            action_type = param.split('=')[1]

    if action == 'send_message':
        if action_type == 'flex':
            flex_obj = FlexSendMessage.new_from_json_dict(
                common_const.const.FLEX)
            line_bot_api.reply_message(
                line_event.reply_token, flex_obj)
        elif action_type == 'carousel':
            carousel_template_message = common_const.const.CAROUSEL
            line_bot_api.reply_message(
                line_event.reply_token, carousel_template_message)
        elif action_type == 'message':
            line_bot_api.reply_message(
                line_event.reply_token, TextSendMessage(text='通常メッセージの送信デモ'))
        else:
            line_bot_api.reply_message(
                line_event.reply_token, TextSendMessage(
                    text='Demonstration of sending Normal Message'))
    elif action == 'change_menu':
        logger.debug('change_menu: ' + action_type)
        line_bot_api.link_rich_menu_to_user(
            line_event.source.user_id,
            common_const.const.MENU_LIST[action_type])
    elif action == 'reserve':
        logger.debug(line_event.postback.params)
        message = str(line_event.postback.params['datetime']) + 'に予約しました！'
        line_bot_api.reply_message(line_event.reply_token,
                                   TextSendMessage(text=message))
    elif action == 'quick_reply':
        items = common_const.const.QUICK_REPLY_ITEMS
        messages = [
            TextSendMessage(text='クイックリプライメニュー',
                            quick_reply=QuickReply(items=items)),
            TextSendMessage(text='「位置情報」を送信する機能を希望しない場合は、端末の「位置情報共有」をオフにしてください。',  # noqa 501
                            quick_reply=QuickReply(items=items))]
        line_bot_api.reply_message(
            line_event.reply_token,
            messages=messages)


@handler.add(FollowEvent)
def follow(line_event):
    """
    Webhookに送信されたLINEフォローイベントについて処理を実施する

    Parameters
    ----------
    line_event: dict
        LINEメッセージイベント内容。

    """
    # デフォルトのリッチメニューを表示する
    line_bot_api.link_rich_menu_to_user(
        line_event.source.user_id,
        common_const.const.MENU_LIST['message'])
