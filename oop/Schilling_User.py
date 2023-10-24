class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self


    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"You don't have enough points for this purchase, current points: {self.gold_card_points}")
            return self
        
        else:    
            self.gold_card_points = self.gold_card_points - amount
            print(f"You now have {self.gold_card_points} points left")
            return self



jarrod = User("Jarrod", "Schilling", "checkit@email.com", 38)
jarrod.display_info().enroll().spend_points(50).display_info().enroll()

piper = User("Piper", "Pied", "piedpiper@piper.com", 22)
nelson = User("Big", "Head", "bighead@hooli.com", 20)

piper.enroll().spend_points(80).display_info()

nelson.display_info().spend_points(40)