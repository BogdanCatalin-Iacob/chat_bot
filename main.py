'''
Chat Bot
'''
from difflib import get_close_matches


def get_best_match(user_input: str, questions: dict) -> str | None:
    '''
    Matches user input question with a preset question
    '''
    questions: list[str] = [question for question in questions]
    # match must be at least 60% to be a valid response
    matches: list = get_close_matches(user_input, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]
