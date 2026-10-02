def explain_topic(topic: str) -> str:
    if not topic or not topic.strip():
        return "Please enter a topic."

    return (
        f"Here is a simple explanation of {topic}.\n\n"
        f"{topic} is an important learning concept. "
        f"EduGenie can help you understand it step by step "
        f"with examples and practice questions."
    )