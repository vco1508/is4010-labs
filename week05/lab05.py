"""Utilities for working with user age and email data."""


def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid."""
    valid_ages = []

    for user in users or []:
        if not isinstance(user, dict):
            continue

        age = user.get("age")

        if age is None or isinstance(age, bool):
            continue

        if isinstance(age, (int, float)):
            valid_ages.append(float(age))
            continue

        if isinstance(age, str):
            try:
                numeric_age = float(age)
            except ValueError:
                continue
            valid_ages.append(numeric_age)

    if not valid_ages:
        return 0.0

    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users):
    """Return email addresses belonging to active users."""
    active_emails = []

    for user in users or []:
        if not isinstance(user, dict):
            continue

        if not user.get("is_active"):
            continue

        if "email" not in user:
            continue

        email = user.get("email")
        if isinstance(email, str) and email:
            active_emails.append(email)

    return active_emails
