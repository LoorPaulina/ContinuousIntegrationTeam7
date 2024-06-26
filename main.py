class GymMembership:

    #yoser
    def get_discount(self):
        if self.total_cost > 400:
            self.total_cost -= 50
        elif self.total_cost > 200: 
            self.total_cost -= 20 

    def premiun_membership(self):
        self.total_cost = self.total_cost * 1.5 #premium membership cost 50% more