import inquirer
from inquirer.themes import GreenPassion
from inquirer.themes import load_theme_from_dict

dict_theme = {
    "Question": {
        "mark_color": "bold_blue",
        "brackets_color": "dodgerblue",
    },
    "List": {
        "selection_color": "deepskyblue2",
        "selection_cursor": "🤖"
    },
    "Checkbox": {
        "selection_color": "deepskyblue2",
        "selection_icon": "->",
        "selected_color": "deepskyblue",
        "unselected_icon": "[ ]",
        "selected_icon": "🤖",
    },
}
custom_theme = inquirer.themes.load_theme_from_dict(dict_theme)


questions = [
    inquirer.Text('search_key', 
                  message="Please enter job position you are looking for",
                  validate=lambda _, x: x != '' and len(x) > 2
                  ),
    inquirer.List('remote',
                message="Please enter if you want remote job or not",
                choices=['True', 'False'],
                
            ),
    inquirer.List('easy_apply',
                message="Please enter if you want easy apply jobs or not",
                choices=['True', 'False'],
            ),
    inquirer.Checkbox('experience_level',
                message="Please enter experience level (press space to select multiple fields)",
                choices=["Internship", "Entry level", "Associate", "Mid-Senior level", "Director", "Executive", 'Choose all'],
            ),
    inquirer.List('number_of_jobs',
                  message="Please enter number of jobs you want to apply",
                  choices=['max', 'choose number of jobs'],
                    ),
]


def menu():
    answers = inquirer.prompt(questions, theme=custom_theme)    
    for number, answer in enumerate(answers):
        if answers[answer] == 'choose number of jobs':
            question = inquirer.Text('number_of_jobs', 
                                     message="Please enter number of jobs you want to apply",
                                     validate=lambda _, x: x != '' and x.isnumeric() and int(x) > 0),
            answers[answer] = int(inquirer.prompt(question, theme=custom_theme)['number_of_jobs'])
        elif answer == 'experience_level' and 'Choose all' in answers[answer]:
            answers[answer] = questions[number].choices[:-1]
    return answers