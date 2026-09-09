from enum import Enum

class OfferCategory(Enum):
    CONSOLE = "console"
    CONTROLLER = "controller"
    GAME = "game"
    ACCESSORY = "accessory"
    BUNDLE = "bundle"
    OTHER = "other"

def classify_offer(message: str) -> OfferCategory | None:
    normalized_message = message.strip().lower()

    if not _is_playstation_related(normalized_message):
        return None

    if _is_bundle(normalized_message):
        return OfferCategory.BUNDLE

    if _is_controller(normalized_message):
        return OfferCategory.CONTROLLER

    if _is_console(normalized_message):
        return OfferCategory.CONSOLE

    if _is_accessory(normalized_message):
        return OfferCategory.ACCESSORY

    if _is_game(normalized_message):
        return OfferCategory.GAME

    return OfferCategory.OTHER
    
def _is_playstation_related(message: str) -> bool:
    keywords = [
        "ps5",
        "playstation",
        "playstation 5",
        "dual sense",
        "dualsense",
    ]

    return any(keyword in message for keyword in keywords)

def _is_console(message: str) -> bool:
    keywords = [
        "console",
        "ps5",
        "slim",
        "digital",
        "leitor",
        "disco",
        "pro",
        "®"
    ]

    return any(keyword in message for keyword in keywords)

def _is_controller(message: str) -> bool:
    keywords = [
        "dualsense",
        "dual sense",
        "controle playstation",
        "controle ps5",
    ]

    return any(keyword in message for keyword in keywords)

def _is_game(message: str) -> bool:
    game_keywords = [
        "jogo",
        "game",
        "-"
    ]

    return any(
        keyword in message
        for keyword in game_keywords
    )

def _is_accessory(message: str) -> bool:
    keywords = [
        "capa",
        "case",
        "suporte",
        "carregador",
        "charging station",
    ]

    return any(keyword in message for keyword in keywords)

def _is_bundle(message: str) -> bool:
    has_console = _is_console(message)

    bundle_keywords = [
        "jogo",
        "jogos",
        "bundle",
        " e "
    ]

    has_bundle_keyword = any(
        keyword in message
        for keyword in bundle_keywords
    )

    return has_console and has_bundle_keyword
