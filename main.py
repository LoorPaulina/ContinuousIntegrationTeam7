class GymMembership:
  
    def __init__(self):
        self.membership_plans = {
        'Basic': {'cost': 50, 'benefits': ['Access to gym equipment']},
        'Premium': {'cost': 100, 'benefits': ['Access to gym equipment', 'Access to exclusive gym facilities', 'Specialized training programs']},
        'Family': {'cost': 150, 'benefits': ['Access to gym equipment', 'Family access for up to 4 members']}
        }

    def display_membership_plans(self):
        print("Available Membership Plans:")
        for plan, details in self.membership_plans.items():
            print(f"{plan}: ${details['cost']} - Benefits: {', '.join(details['benefits'])}")

    def select_membership_plan(self, plan_name, num_members=1):
        if plan_name in self.membership_plans:
            self.selected_plan = plan_name
            self.num_members = num_members
        else:
            raise ValueError("Invalid membership plan selected.")

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