def classify_intent(text: str) -> str:
    automation_keywords = ["open", "close", "play", "start"]

    for word in automation_keywords:
        if word in text:
            return "automation"

    return "query"
if __name__ == "__main__":
    print(classify_intent("open chrome"))
    print(classify_intent("what is AI"))