

#Part_1


def Padel_court_cost(court_type):
    if court_type == "Indoor":
        return 30
    elif court_type == "Outdoor":
        return 20


#Part_2


def Racket_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return 100
    elif racket_brand == "Nox":
        return 140
    elif racket_brand == "Siux":
        return 200


#Part_3


def Padle_balls_cost(ball_boxes):
    if int(ball_boxes) == 1:
        return 2
    elif int(ball_boxes) == 2:
        return 3.5
    elif int(ball_boxes) == 3:
        return 5


#Part_4


def Padle_game_cost():
    court_type = input (" Indoor or Outdoor? ")
    racket_brand = input (" Bullpadle , Nox or Siux? ")
    ball_boxes = int (input (" 1 , 2 or 3 boxes? "))
    
    Total_cost = Padel_court_cost(court_type) + Racket_cost(racket_brand) + Padle_balls_cost(ball_boxes)
    
    print (f"""
           Court: {court_type}
           Racket Brand: {racket_brand}
           Number of the Boxes: {ball_boxes}
           """)
    return Total_cost

Total_price = Padle_game_cost()

print (f"Your total price is: {Total_price} KD")