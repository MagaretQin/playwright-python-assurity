import logging.config
import requests




def test_api_response():
    url = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"
    response = requests.get(url=url)
    if response.status_code == 200:
        response_dict = response.json()

        # AC1 - Name = "Carbon credits"
        name_value = response_dict["Name"]
        logging.info("Name value: " + name_value)
        assert name_value == "Carbon credits"

        # AC2 - CanRelist = true
        can_relist_value = response_dict["CanRelist"]
        logging.info("CanRelist: " + str(can_relist_value))
        assert can_relist_value

        # AC3 - The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
        promotions_list = response_dict["Promotions"]
        for item in promotions_list:
            if item["Name"] =="Gallery":
                description = item["Description"]
                logging.info("Gallery description: " + str(description))
                assert "Good position in category" in description



        logging.info("TEST PASSED")

    else:
        raise Exception(f'API status check failed: {response.status_code}')
