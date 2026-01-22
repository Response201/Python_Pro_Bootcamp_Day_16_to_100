from turtle import Screen,textinput,Turtle
import pandas
from state_label import State_label
from winner_text import Winner_text


screen = Screen()
screen.setup(700,500)
screen.bgpic("blank_states_img.gif")
screen.title("U.S States Game")


data = pandas.read_csv("50_states.csv")
create_label = State_label()
states_correct = []



# Spelet körs tills alla delstater är gissade
while len(states_correct) < len(data):

    # Frågar spelaren efter en ny delstat
    find_state_input = textinput(f"{len(states_correct)}/{len(data)} States Correct", "Whats another state name?")

    # Om användaren trycker på "cancel" avslutas spelet
    if find_state_input is None:
        screen.tracer(0)

        # Går igenom alla stater från cvs-fil och hantera de som inte hittats (sparats i listan states_correct)
        missing_states = [state for state in data["state"] if state not in states_correct]

        for state in missing_states:

                    create_label.data = data[data.state == state]
                    create_label.not_found_labels()


        screen.update()
        break


    find_state = find_state_input.title()

    # Kontrollerar att delstaten inte redan gissats
    if find_state not in states_correct:

        # Om delstaten finns kommer längden att vara större än 0
        existing_state_row = data[data.state == find_state]

        if len(existing_state_row) >= 1:
            states_correct.append(find_state)
            create_label.data = existing_state_row
            create_label.create_label()



# När alla delstater är hittade visas vinnartext
if len(states_correct) >= len(data):
    Winner_text()



screen.mainloop()