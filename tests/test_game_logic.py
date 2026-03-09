from logic_utils import check_guess

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
