from masks import get_mask_account, get_mask_card_number
from widget import get_date, mask_account_card

acc_num = 73654108430135874305
card_num = 1234567812345678

check_data = "2024-03-11T02:26:18.671407"
card = "Visa Platinum 8990922113665229"

print(get_mask_card_number(card_num))
print(get_mask_account(acc_num))

print(mask_account_card(card))
print(get_date(check_data))
