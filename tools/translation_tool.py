from deep_translator import GoogleTranslator


def execute(arguments: dict[str, str]) -> str:
    """Translate the provided text using Google Translate.

    Expected arguments:
    {
        "text": "...",
        "target_language": "...",
        "source_language": "auto"
    }
    """
    text = arguments.get("text")
    target_language = arguments.get("target_language")
    source_language = arguments.get("source_language", "auto")

    if not text:
        raise ValueError("Missing 'text' argument for translation.")

    if not target_language:
        raise ValueError("Missing 'target_language' argument for translation.")

    translator = GoogleTranslator(source=source_language, target=target_language)
    return translator.translate(text)
