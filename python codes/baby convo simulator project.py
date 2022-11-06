from random import choice

questions=["Why is the sky blue?","Why does the sun rise in the east","Where all the dinosaurs"]
question=choice(questions)
answer=input("Why is the sky blue?:").lower()
while answer!="just because":
    answer=input("why?:").strip().lower()
print("OH...Okay") 
    
