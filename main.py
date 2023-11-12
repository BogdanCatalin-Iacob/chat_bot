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


def chat_bot(knowledge: dict):
    '''
    Returns back to user an answer of a matching question
    found in the knowledge dict
    '''
    while True:
        user_input: str = input('You: ')
        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t understand the question!')


if __name__ == '__main__':
    knowledge_base: dict = {
        'hello': 'Hey there!',
        'how are you': 'I\'m good, thanks!',
        'What time is it': 'I have no clue...',
        'bye': 'Hasta la vista :D'
    }

    chat_bot(knowledge_base)
