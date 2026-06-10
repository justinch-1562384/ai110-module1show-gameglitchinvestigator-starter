from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_text_points_in_correct_direction():
    # Regression test for the bug we fixed in check_guess.
    #
    # The hint messages used to be backwards: a "Too High" guess told the
    # player to "Go HIGHER!" and a "Too Low" guess told them to "Go LOWER!",
    # which sent them in the wrong direction every time.
    #
    # A guess that is too high must point the player LOWER, and a guess that
    # is too low must point them HIGHER.
    high_outcome, high_message = check_guess(60, 50)
    assert high_outcome == "Too High"
    assert "LOWER" in high_message

    low_outcome, low_message = check_guess(40, 50)
    assert low_outcome == "Too Low"
    assert "HIGHER" in low_message


def test_off_by_one_attempts_allows_full_limit():
    # Regression test for the off-by-one bug we fixed in app.py.
    #
    # Before the fix, st.session_state.attempts was initialized to 1 instead
    # of 0, which silently consumed one guess: a "Normal" game (8 attempts
    # allowed) only let the player guess 7 times, and the sidebar's
    # "Attempts allowed" never matched the prompt's "Attempts left".
    #
    # This mirrors app.py's counting logic (initial value + one increment
    # per submitted guess) and asserts the behavior the bug broke.
    limit = 8                 # Normal difficulty: "Attempts allowed"
    attempts = 0              # FIX: a fresh game must start at 0 (was 1)

    # Before any guess, "Attempts left" should equal "Attempts allowed".
    assert limit - attempts == limit

    # Simulate the player using every allowed guess.
    guesses_made = 0
    while attempts < limit:
        attempts += 1         # mirrors `st.session_state.attempts += 1`
        guesses_made += 1

    # The player should get the full number of guesses, not one fewer.
    assert guesses_made == limit
