import streamlit as st
import random

# Initialize session state for boss health
if 'Bhp' not in st.session_state:
    st.session_state.Bhp = 100

def game():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)

    dice_dict = {"1": d1, "2": d2, "3": d3}

    st.write(f"Boss Health = {st.session_state.Bhp}")
    st.write(f"Available dice: {d1}, {d2}, {d3}")

    choice = st.text_input("Which dice do you want to use? (Enter 1, 2, or 3)")
    if st.button('Attack'):
        if choice in dice_dict:
            dice_value = dice_dict[choice]
            if dice_value <= 3:
                st.write(f"Dealt {dice_value} damage")
                st.session_state.Bhp -= dice_value
            else:
                chance = random.randint(0, 1)
                if chance == 0:
                    st.write("The attack missed and you dealt no damage")
                else:
                    st.write(f"Dealt {dice_value * 1.5} damage")
                    st.session_state.Bhp -= (dice_value * 1.5)
        else:
            st.write("Invalid choice. Please enter 1, 2, or 3.")

    # Refresh the page to see the updated values
    if st.button('Refresh'):
        st.session_state.Bhp = 100

# Run the game function
game()










