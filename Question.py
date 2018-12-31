from typing import Any


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)
