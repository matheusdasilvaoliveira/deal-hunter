from src.services.ps5_detector import is_ps5_message

def test_should_detect_ps5():
    message = "PS5 Slim Digital por R$ 3.299"
    
    assert is_ps5_message(message)

def test_should_not_detect_other_consoles():
    message = "Xbox Series S por R$ 1.999"

    assert not is_ps5_message(message)
    
def test_should_detect_ps5_case_insensitive():
    message = "PlayStation 5 Slim por R$ 3.499"

    assert is_ps5_message(message)
    
def test_should_detect_ps5_without_space():
    message = "PlayStation5 por R$ 3.299"

    assert is_ps5_message(message)