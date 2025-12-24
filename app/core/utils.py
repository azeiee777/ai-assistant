import re

def is_greeting(text: str) -> bool:
    greetings = {
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    }
    return text.lower().strip() in greetings

def is_invalid_input(text: str) -> bool:
    if not text:
        return True

    cleaned = text.strip()

    # Case 1: Empty or whitespace only
    if not cleaned:
        return True

    # Case 2: Only symbols / punctuation
    if re.fullmatch(r"[\W_]+", cleaned):
        return True

    # Case 3: Very short meaningless input (e.g. ".", "..", "?")
    if len(cleaned) <= 2 and not cleaned.isalnum():
        return True

    return False
