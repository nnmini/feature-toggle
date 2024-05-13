# Define sample intents and entities
intents = {
    "select_row": ["select", "choose", "pick"],
    "perform_action": ["edit", "delete", "update"],
    "get_data": ["fetch", "show", "display"],
    "help": ["help", "assist", "guide"],
}

entities = {
    "row_number": ["1", "2", "3", "4"],
    "action_type": ["edit", "delete", "update"],
    "filter_criteria": ["price", "model", "make"],
}


def process_input(user_input):
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
                if intent == "select_row":
                    row_number = extract_row_number(user_input)
                    if row_number is not None:
                        return f"Selected row {row_number}."
                elif intent == "perform_action":
                    action, row_number = extract_action_and_row(user_input)
                    if action is not None and row_number is not None:
                        return f"Performed {action} action on row {row_number}."
                elif intent == "get_data":
                    criteria = extract_criteria(user_input)
                    if criteria is not None:
                        return f"Fetched data based on {criteria}."
                elif intent == "help":
                    return "Here are some commands you can use:\n- Select row [number]\n- Perform [action] on row\n- Fetch data by [criteria]"

    return "Sorry, I didn't understand that. Type 'help' for assistance."


def extract_action_and_row(user_input):
    actions = ["edit", "update", "modify"]
    for action in actions:
        if action in user_input:
            row_number = extract_row_number(user_input)
            return action, row_number
    return None, None


def extract_row_number(user_input):
    # Code to extract the row number from user input
    words = user_input.split()
    for word in words:
        if word.isdigit():
            return int(word)
    return None


def extract_action(user_input):
    # Code to extract the action from user input
    actions = ["edit", "update", "modify"]
    for action in actions:
        if action in user_input:
            return action
    return None


def extract_criteria(user_input):
    # Code to extract the criteria from user input
    criteria_keywords = ["criteria", "filter"]
    for keyword in criteria_keywords:
        if keyword in user_input:
            # Extract the criteria following the keyword
            index = user_input.index(keyword)
            return user_input[index + len(keyword) + 1 :]
    return None


# Main loop to simulate chat interaction
print("Welcome to the Table Chatbot! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = process_input(user_input.lower())
    print("Chatbot:", response)
