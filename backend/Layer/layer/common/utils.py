"""
共通関数
"""


def create_response(status_code, body):
    """
    フロントに返却するデータを作成する

    Parameters
    ----------
    status_code : int
        フロントに返却するステータスコード
    body:dict,str
        フロントに返却するbodyに格納するデータ
    Returns
    -------
    response : dict
        フロントに返却するデータ
    """
    response = {
        'statusCode': status_code,
        'headers': {"Access-Control-Allow-Origin": "*"},
        'body': body
    }
    return response


def create_error_response(body, status=500):
    """
    エラー発生時にフロントに返却するデータを作成する

    Parameters
    ----------
    body : dict,str
        フロントに返却するbodyに格納するデータ
    status:int
        フロントに返却するステータスコード
    Returns
    -------
    create_response:dict
        フロントに返却するデータ
    """
    return create_response(status, body)


def create_success_response(body):
    """
    正常終了時にフロントに返却するデータを作成する

    Parameters
    ----------
    body : dict,str
        フロントに返却するbodyに格納するデータ
    Returns
    -------
    create_response:dict
        フロントに返却するデータ
    """
    return create_response(200, body)
