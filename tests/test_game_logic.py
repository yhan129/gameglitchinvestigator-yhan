from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_says_lower():
    # FIX verified: when guess is too high, message should say Go LOWER
    _, message = check_guess(99, 1)
    assert "LOWER" in message

def test_too_low_message_says_higher():
    # FIX verified: when guess is too low, message should say Go HIGHER
    _, message = check_guess(1, 99)
    assert "HIGHER" in message

# --- Edge-case tests (Challenge 1) ---

def test_negative_guess_too_low():
    # A negative number should be treated as Too Low against any positive secret
    outcome, _ = check_guess(-5, 50)
    assert outcome == "Too Low"

def test_decimal_input_rounds_and_works():
    # parse_guess should convert "3.9" to int 3, which is then Too Low vs 50
    ok, value, err = parse_guess("3.9")
    assert ok is True
    assert value == 3
    outcome, _ = check_guess(value, 50)
    assert outcome == "Too Low"

def test_very_large_guess_too_high():
    # An extremely large number should be Too High against any normal secret
    outcome, _ = check_guess(999999, 100)
    assert outcome == "Too High"

def test_empty_input_rejected():
    # An empty string should fail parsing and return an error message
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_text_input_rejected():
    # A non-numeric string should fail parsing
    ok, value, err = parse_guess("hello")
    assert ok is False
    assert err == "That is not a number."

def test_none_input_rejected():
    # None input should fail gracefully
    ok, value, err = parse_guess(None)
    assert ok is False
