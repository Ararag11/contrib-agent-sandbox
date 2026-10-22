"""Tiny text statistics helpers (sandbox for contrib-agent end-to-end tests)."""


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split(" "))


def average_word_length(text: str) -> float:
    """Return the mean word length; 0.0 for empty input."""
    words = text.split()
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)
