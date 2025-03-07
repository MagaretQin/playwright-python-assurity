from apps.api.tmsandbox import tmsandbox_api



def test_validate_tmsandbox():
    response = tmsandbox_api.request_tmsandbox()
    # AC1 - Name = "Carbon credits"
    tmsandbox_api.check_category_name(response)
    # AC2 - CanRelist = true
    tmsandbox_api.check_can_relist(response)
    # AC3 - The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
    tmsandbox_api.check_promotion_item_des(response, item_name="Gallery", exp_item_des="Good position in category")

