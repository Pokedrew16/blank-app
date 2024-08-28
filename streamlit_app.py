import streamlit as st
import random

st.title("🎈 BMI calculator")
st.write(
    "Welcome to the BMI calculator."
)
Bhp = 100
def game():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)

    dict = {"d1": d1, "d2": d2, "d3": d3}
    
    st.write(f"Boss Health = {Bhp}")   
    st.write(f"Availble dice: {d1}, {d2}, {d3}")


    
    choice = st.text_input("What dice do you want to use.")
    if st.button('Attack'):
        if dict[choice] <= 3:
            st.write(f"Dealt {dict[choice]} dmg")
            Bhp += -dict[choice]
            game()
        elif dict[choice] >= 4:
            chance = random.randint(0,1)
            if chance == 0:
                st.write("The attack missed and you dealt no dmg")
                game()
            elif chance == 1:
                st.write(f"Dealt {dict[choice] ^ 1.5} dmg")
                game()
game()









