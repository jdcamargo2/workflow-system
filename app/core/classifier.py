def classify_text(text: str) -> str:
    text = text.lower().strip()

    study_keywords = ["estudiar", "repasar", "leer", "practicar", "resolver"]
    task_keywords = ["comprar", "hacer", "ir", "pagar", "enviar", "llamar"]

    if any(word in text for word in study_keywords):
        return "study"

    if any(word in text for word in task_keywords):
        return "task"

    return "note"