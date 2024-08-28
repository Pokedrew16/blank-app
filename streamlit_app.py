import streamlit as st
import random

# Initialize session state for boss health and dice values
if 'Bhp' not in st.session_state:
    st.session_state.Bhp = 100
if 'dice_values' not in st.session_state:
    st.session_state.dice_values = {"1": 0, "2": 0, "3": 0}

def roll_dice():
    # Roll the dice and update session state
    st.session_state.dice_values = {
        "1": random.randint(1, 6),
        "2": random.randint(1, 6),
        "3": random.randint(1, 6)
    }

def game():
    roll_dice()
    d1, d2, d3 = st.session_state.dice_values.values()
    
    st.write(f"Boss Health = {st.session_state.Bhp}")
    st.write(f"Available dice: {d1}, {d2}, {d3}")

    choice = st.text_input("Which dice do you want to use? (Enter 1, 2, or 3)")
    
    if st.button('Attack'):
        if choice in st.session_state.dice_values:
            dice_value = st.session_state.dice_values[choice]
            if dice_value <= 3:
                st.write(f"Dealt {dice_value} damage")
                st.session_state.Bhp -= dice_value
            else:
                chance = random.randint(0, 1)
                if chance == 0:
                    st.write("The attack missed and you dealt no damage")
                else:
                    damage = dice_value * 1.5
                    st.write(f"Dealt {damage:.0f} damage")  # Display as integer
                    st.session_state.Bhp -= damage
        else:
            st.write("Invalid choice. Please enter 1, 2, or 3.")

    if st.button('Refresh'):
        st.session_state.Bhp = 100
        roll_dice()

# Run the game function
game()











