from requests import Response
import json
from typing import Any,List,Dict
def mock_get_conversations(*args:List[Any],**kwargs:Dict[str,Any])->Response:
    """mock for convesations list

    Returns:
        Response: _description_
    """
    result={"ok": "true",
        "channels": [
        {
            "id": "C086YFZ9DDL",
            "name": "all-shilpa",
            "is_channel": "true",
            "is_group": "false",
            "is_im": "false",
            "updated": 1735880230018,
            "shared_team_ids": [
                "T0877KXMYAY"
            ],}]}
    
    url="https://slack.com/api/get_convesations"
    response=Response()
    response.status_code=200
    response._content=bytes(json.dumps(result),encoding="utf-8")
    return response


def mock_list_conversation_fail(*args:List[Any],**kwargs:Dict[str,Any])->Response:
    """_summary_
    Returns:
        Response: _description_
    """
    result={
        "error":"Invalid authorization"
    }
    url='https://slack.com/api/conversations.list'
    response=Response()
    response.url=url
    response.status_code=404
    response._content=bytes(json.dumps(result),encoding="utf-8")
    return response