import logging.config
import requests
from utils.endpoint_builder import build_url_api


def request_tmsandbox():
    url = build_url_api(app="tmsandbox", category=6327)
    response = requests.get(url=url)

    if response.status_code == 200:
        logging.info("Response status: %s", response.status_code)
        response_dict = response.json()
        return response_dict
    else:
        logging.info("Response status: %s", response.status_code)
        raise Exception(f'API status check failed: {response.status_code}')

def check_category_name(response):
    name_value = response["Name"]
    logging.info("Name value: " + name_value)
    assert name_value == "Carbon credits"

def check_can_relist(response):
    can_relist_value = response["CanRelist"]
    logging.info("CanRelist: " + str(can_relist_value))
    assert can_relist_value

def check_promotion_item_des(response, item_name, exp_item_des):
    """
            Args:
                response: JSON response based on request.
                item_name: str item needs to be checked under Promotions list.
                exp_item_des: str expected item description.
            """
    promotions_list = response["Promotions"]
    for item in promotions_list:
        if item["Name"] == item_name:
            description = item["Description"]
            logging.info(f"{item_name} description: " + str(description))
            assert exp_item_des in description
            break
    else:
        raise ValueError(f'No existing item -- {item_name} in the list')
