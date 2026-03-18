from nemoguardrails import action

@action()
def contains_personal_question(user_input: str) -> bool:
    
    blocked_keywords = [
        "lover",
        "girlfriend",
        "boyfriend",
        "relationship",
        "dating",
        "married",
        "wife",
        "husband"
        "india"
        "animal"
        "fruits"
    ]

    text = user_input.lower()

    return any(word in text for word in blocked_keywords)