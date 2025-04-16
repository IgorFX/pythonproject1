from masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Возвращает название карты и маскиолваный номер карты(счета)"""

    account_card = card.split()

    if account_card[0] == "Счет":
        masked_account = get_mask_account(int(account_card[1]))
        return f"{account_card[0]} {masked_account}"
    else:
        if len(account_card) > 2:
            card_name = f"{account_card[0]} {account_card[1]}"
        else:
            card_name = f"{account_card[0]}"
        masked_card = get_mask_card_number(int(account_card[-1]))

    return f"{card_name} {masked_card}"


def get_date(date: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГ"""

    clear_date = date.split("T")[0].split("-")
    day = clear_date[2]
    month = clear_date[1]
    year = clear_date[0]
    new_data = f"{day}.{month}.{year}"

    return new_data
