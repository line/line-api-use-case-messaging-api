"""
Constant types in Python.
定数上書きチェック用
"""
import os
from common import const
from datetime import timedelta

from linebot.models import (
    TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageAction,
    QuickReplyButton, CameraAction, CameraRollAction, LocationAction
)

const.API_PROFILE_URL = 'https://api.line.me/v2/profile'
const.API_NOTIFICATIONTOKEN_URL = 'https://api.line.me/message/v3/notifier/token'  # noqa: E501
const.API_SENDSERVICEMESSAGE_URL = 'https://api.line.me/message/v3/notifier/send?target=service'  # noqa 501
const.API_USER_ID_URL = 'https://api.line.me/oauth2/v2.1/verify'

const.MSG_ERROR_NOPARAM = 'パラメータ未設定エラー'
const.DATA_LIMIT_TIME = 60 * 60 * 12
const.ONE_WEEK = timedelta(days=7)
const.JST_UTC_TIMEDELTA = timedelta(hours=9)


const.FLEX = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://media.istockphoto.com/photos/empty-coffee-shop-picture-id1154756901",  # noqa:E501
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover",
            "action": {
                "type": "uri",
                "label": "UseCase Cafe",
                "uri": "https://line.me/ja/"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "LINE Cafe",
                    "size": "xl",
                    "weight": "bold"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "icon",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",  # noqa:E501
                            "size": "sm"
                        },
                        {
                            "type": "icon",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",  # noqa:E501
                            "size": "sm"
                        },
                        {
                            "type": "icon",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",  # noqa:E501
                            "size": "sm"
                        },
                        {
                            "type": "icon",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",  # noqa:E501
                            "size": "sm"
                        },
                        {
                            "type": "icon",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",  # noqa:E501
                            "size": "sm"
                        },
                        {
                            "type": "text",
                            "text": "4.0",
                            "flex": 0,
                            "margin": "md",
                            "size": "sm",
                            "color": "#999999"
                        }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "margin": "lg",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Place",
                                    "flex": 1,
                                    "size": "sm",
                                    "color": "#AAAAAA"
                                },
                                {
                                    "type": "text",
                                    "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",  # noqa:E501
                                    "flex": 5,
                                    "size": "sm",
                                    "color": "#666666",
                                    "wrap": True
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Time",
                                    "flex": 1,
                                    "size": "sm",
                                    "color": "#AAAAAA"
                                },
                                {
                                    "type": "text",
                                    "text": "10:00 - 23:00",
                                    "flex": 5,
                                    "size": "sm",
                                    "color": "#666666",
                                    "wrap": True
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "flex": 0,
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "WEBサイト",
                        "uri": "https://line.me/ja/"
                    },
                    "height": "sm",
                    "style": "link"
                },
                {
                    "type": "button",
                    "action": {
                        "type": "datetimepicker",
                        "label": "予約",
                        "data": "action=reserve",
                        "mode": "datetime",
                        "initial": "2020-01-01t00:00",
                        "max": "2020-12-31t23:59",
                        "min": "2020-01-01t00:00"
                    },
                    "height": "sm",
                    "style": "link"
                },
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "クイックアクション",
                        "data": "action=quick_reply",
                    },
                    "height": "sm",
                    "style": "link"
                },
                {
                    "type": "spacer",
                    "size": "sm"
                }
            ]
        }
    }
}

const.CAROUSEL = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://media.istockphoto.com/photos/neon-sale-glowing-text-sign-sale-banner-design-3d-render-glow-sale-picture-id854550186',  # noqa:E501
                title='最大80%OFF',
                text='期間限定SALE',
                actions=[
                    MessageAction(
                        label='Go to SALE',
                        text='Choose SALE'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://media.istockphoto.com/photos/womens-clothes-set-isolatedfemale-clothing-collage-picture-id1067767654',  # noqa:E501
                title='今月のおススメ商品',
                text='これがあれば困らない！',
                actions=[
                    MessageAction(
                        label='Recommended',
                        text='Choose Recommended'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://media.istockphoto.com/photos/clothes-hanging-on-rail-in-white-wardrobe-picture-id518597694',  # noqa:E501
                title='スッキリ収納特集',
                text='大切なお洋服をスッキリ簡単に収納します',
                actions=[
                    MessageAction(
                        label='To receive clothes',
                        text='Choose receive clothes'
                    )
                ]
            )
        ]
    )
)

const.QUICK_REPLY_ITEMS = [
    QuickReplyButton(action=LocationAction(label='位置情報')),
    QuickReplyButton(action=CameraAction(label='カメラ起動')),
    QuickReplyButton(action=CameraRollAction(label='カメラロール起動')),
]

const.MENU_LIST = {'message': os.getenv('RICH_MENU_MESSAGE', None),
                   'carousel': os.getenv('RICH_MENU_CAROUSEL', None),
                   'flex': os.getenv('RICH_MENU_FLEX', None)
                   }
