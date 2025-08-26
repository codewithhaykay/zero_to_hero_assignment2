from typing import Dict

VOWELS = set("aeiou")

def analyze_name(full_name: str) -> Dict[str, str | int]:
    """
    Analyze a person's full name and return multiple transformations and stats.

    Returns a dict with:
      - uppercase
      - lowercase
      - titlecase
      - initials
      - char_count_no_spaces
      - vowel_count
    Raises:
      ValueError if the name contains characters other than letters and whitespace
      or if the normalized name is empty.
    """
    # Normalize: strip outer spaces and collapse internal whitespace to single spaces
    normalized = " ".join(full_name.split())

    # Ensure we still have something after normalization
    if not normalized:
        raise ValueError("Invalid name. Please enter a non-empty name.")

    # Validation: allow only alphabetic characters and whitespace (Unicode letters included)
    if not all(ch.isalpha() or ch.isspace() for ch in normalized):
        raise ValueError("Invalid name. Only letters and spaces are allowed.")

    # Precompute lowercase once (used by multiple steps)
    lower_name = normalized.lower()

    # Transformations
    uppercase_name = normalized.upper()
    lowercase_name = lower_name
    titlecase_name = normalized.title()

    # Initials: take first character of each word, uppercase, with dots (e.g., A.L.A.)
    initials = "".join(part[0].upper() + "." for part in normalized.split())

    # Count non-whitespace characters (works for tabs, multiple spaces, etc.)
    char_count_no_spaces = sum(not ch.isspace() for ch in normalized)

    # Count vowels (a, e, i, o, u) in a case-insensitive way
    vowel_count = sum(ch in VOWELS for ch in lower_name)

    return {
        "uppercase": uppercase_name,
        "lowercase": lowercase_name,
        "titlecase": titlecase_name,
        "initials": initials,
        "char_count_no_spaces": char_count_no_spaces,
        "vowel_count": vowel_count,
    }

def creative_full_name() -> str:
    """Prompt for a name, analyze it, and format a user-facing report string."""
    full_name = input("Enter your full name: ")
    try:
        info = analyze_name(full_name)
    except ValueError as e:
        return str(e)

    result = (
        f"Uppercase: {info['uppercase']}\n"
        f"Lowercase: {info['lowercase']}\n"
        f"TitleCase: {info['titlecase']}\n"
        f"Initials: {info['initials']}\n"
        f"Number of characters (without spaces): {info['char_count_no_spaces']}\n"
        f"Number of vowels: {info['vowel_count']}"
    )
    return result

if __name__ == "__main__":
    print(creative_full_name())