PS5_KEYWORDS: list = [
    "ps5",
    "playstation 5",
    "playstation5",
    "play 5"
]

def is_ps5_message(message: str) -> bool:
    normalized_message = message.lower()

    return any(
        keyword in normalized_message
        for keyword in PS5_KEYWORDS
    )
