from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define sample intents and entities
intents = {
    "select_row": ["select", "choose", "pick"],
    "perform_action": ["edit", "delete", "update"],
    "get_data": ["fetch", "show", "display"],
    "add_column": ["enter", "load"],
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
            if keyword.lower() in user_input.lower():
                if intent == "select_row":
                    row_number = extract_row_number(user_input)
                    if row_number is not None:
                        return {"action": "select", "rowNumber": row_number}
                elif intent == "perform_action":
                    action, row_number = extract_action_and_row(user_input)
                    if action is not None and row_number is not None:
                        return {"action": action, "rowNumber": row_number}
                elif intent == "get_data":
                    criteria = extract_criteria(user_input)
                    if criteria is not None:
                        return {"action": "fetch", "criteria": criteria}
                elif intent == "add_column":
                    make_values = extract_make_values(user_input)
                    if make_values:
                        return {
                            "action": "add column",
                            "column": "make",
                            "values": make_values,
                        }
                elif intent == "help":
                    return {
                        "response": "Here are some commands you can use:\n- Select row [number]\n- Perform [action] on row\n- Fetch data by [criteria]"
                    }

    return {"response": "Sorry, I didn't understand that. Type 'help' for assistance."}


def extract_make_values(user_input):
    # Code to extract make values from user input
    if "make" in user_input:
        # Split the input string by "make"
        parts = user_input.split("make")
        print("Make values extracted:", parts)
        if len(parts) > 1:
            # Get the part after "make"
            values_part = parts[1].strip()
            # Split the values by space and remove empty strings
            make_values = [
                value.strip() for value in values_part.split() if value.strip()
            ]
            return make_values
    return None


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


@app.route("/process_user_input", methods=["POST"])
def process_user_input():
    user_input = request.json.get("user_input")
    response = process_input(user_input)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
