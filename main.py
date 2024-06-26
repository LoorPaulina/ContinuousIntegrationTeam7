class GymMembership:
    #katherine tumbaco
    def add_additional_features(self, features):
      for feature in features:
        if feature not in self.additional_features:
          self.selected_features.append(feature)

    #yoser
    def get_discount(self):
        if self.total_cost > 400:
            self.total_cost -= 50
        elif self.total_cost > 200: 
            self.total_cost -= 20 

    def premiun_membership(self):
        self.total_cost = self.total_cost * 1.5 #premium membership cost 50% more
