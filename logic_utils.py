def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """
    Return the (low, high) inclusive number range for a given difficulty level.

    Args:
        difficulty: One of "Easy", "Normal", or "Hard".

    Returns:
        A tuple (low, high) representing the inclusive guess range.
        Defaults to (1, 100) for unrecognized difficulty values.

    Examples:
        >>> get_range_for_difficulty("Easy")
        (1, 20)
        >>> get_range_for_difficulty("Hard")
        (1, 1000)
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 1000
    return 1, 100


def parse_guess(raw: str) -> tuple[bool, int | None, str | None]:
    """
    Parse a raw string input from the user into an integer guess.

    Handles None, empty strings, decimal strings (e.g. "3.9" -> 3),
    and non-numeric strings gracefully without raising exceptions.

    Args:
        raw: The raw string entered by the user.

    Returns:
        A tuple of (ok, guess_int, error_message):
            - ok (bool): True if parsing succeeded, False otherwise.
            - guess_int (int | None): The parsed integer, or None on failure.
            - error_message (str | None): A user-facing error string, or None on success.

    Examples:
        >>> parse_guess("42")
        (True, 42, None)
        >>> parse_guess("hello")
        (False, None, 'That is not a number.')
        >>> parse_guess("")
        (False, None, 'Enter a guess.')
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """
    Compare a player's guess to the secret number and return the outcome.

    Args:
        guess: The integer the player guessed.
        secret: The secret integer the player is trying to find.

    Returns:
        A tuple of (outcome, message):
            - outcome (str): One of "Win", "Too High", or "Too Low".
            - message (str): A user-facing hint string with emoji.

    Examples:
        >>> check_guess(50, 50)
        ('Win', '🎉 Correct!')
        >>> check_guess(60, 50)
        ('Too High', '📉 Go LOWER!')
        >>> check_guess(40, 50)
        ('Too Low', '📈 Go HIGHER!')
    """
    # FIX: Refactored from app.py; corrected swapped higher/lower messages
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """
    Calculate the new score based on the outcome of a guess attempt.

    Winning awards points that decrease with each attempt (minimum 10).
    A "Too High" guess on an even attempt adds 5 points; odd attempts deduct 5.
    A "Too Low" guess always deducts 5 points.

    Args:
        current_score: The player's score before this attempt.
        outcome: The result string — "Win", "Too High", or "Too Low".
        attempt_number: The 1-based attempt count for this guess.

    Returns:
        The updated integer score after applying the outcome.

    Examples:
        >>> update_score(0, "Win", 1)
        80
        >>> update_score(100, "Too Low", 3)
        95
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
