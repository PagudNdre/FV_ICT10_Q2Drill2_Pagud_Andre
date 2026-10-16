from pyscript import document, display




def new_member(e):

    members_7 = {'Andre Pagud', 'Sean Chua', 'Edrian Correa', 'Matt Pagsanhan', 'Sean Ho'}

    members_8 = {'Jacob Minguillo', 'Kendrick Dino', ' Logan Anaque', 'Jowinson Sy', 'Marcus De Jesus'}

    members_9 = {'Jan Cabading', 'Raphael Buan', 'Dustin Cunanan', 'Julia Bermudez','Mateo Salacup'}

    members_10 = {'Kyn Tunggalian', 'Joaquin Castor', 'Finn Hizon', 'Danielle Sandoval','Jericho Magsalin'}

    First = document.getElementById("First_name").value
    Last = document.getElementById("Second_name").value

    combined = members_7 | members_8 | members_9 | members_10

    display(combined, target="output")

    combined.add(First + Last)

    


