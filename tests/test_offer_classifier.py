from src.services.offer_classifier import (
    OfferCategory,
    classify_offer,
)


def test_should_classify_gta_6_as_game():
    message = """
    Grand Theft Auto VI - PlayStation 5

    359,92 no pix
    """

    assert classify_offer(message) == OfferCategory.GAME


def test_should_classify_dualsense_as_controller():
    message = """
    Controle Playstation Dualsense Midnight Black

    306,27 no pix
    """

    assert classify_offer(message) == OfferCategory.CONTROLLER


def test_should_classify_ps5_slim_digital_as_console():
    message = """
    Console PlayStation 5 Slim Edição Digital

    3.204,05 no pix
    """

    assert classify_offer(message) == OfferCategory.CONSOLE


def test_should_classify_ps5_with_games_as_bundle():
    message = """
    PlayStation 5 Slim Digital 825GB
    ASTRO BOT e Gran Turismo 7

    3.255,12 no pix
    """

    assert classify_offer(message) == OfferCategory.BUNDLE


def test_should_classify_console_with_two_games_as_bundle():
    message = """
    Console PlayStation 5 Slim Edição Digital + 2 Jogos

    2.689,07 no pix
    """

    assert classify_offer(message) == OfferCategory.BUNDLE


def test_should_ignore_unrelated_message():
    message = """
    Xbox Series S por R$ 1.999
    """

    assert classify_offer(message) is None