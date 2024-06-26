class GymMembership:
    def validate_availability(self):
        if self.selected_plan not in self.membership_plans:
            print(f"Error: The selected membership plan '{self.selected_plan}' is unavailable.")
            return False
        
        for feature in self.selected_features:
            if feature not in self.additional_features:
                print(f"Error: The selected feature '{feature}' is unavailable.")
                return False
        return True
    def confirm_membership(self):
        print("Membership Confirmation:")
        print(f"Selected Plan: {self.selected_plan}")
        print(f"Number of Members: {self.num_members}")
        print(f"Additional Features: {', '.join(self.selected_features)}")
        print(f"Total Cost: ${self.total_cost:.2f}")
        
        confirmation = input("Do you confirm this membership? (yes/no): ")
        if confirmation.lower() == 'yes':
            return self.total_cost
        else:
            return -1

     def calculate_cost(self):
        if not self.selected_plan:
            raise ValueError("No membership plan selected.")
        
        base_cost = self.membership_plans[self.selected_plan]['cost']
        additional_features_cost = sum([self.additional_features[feature] for feature in self.selected_features])
        
        self.total_cost = base_cost + additional_features_cost
        
        if self.num_members >= 2:
            self.total_cost *= 0.9  # Apply 10% discount for group memberships
        
        if self.total_cost > 400:
            self.total_cost -= 50
        elif self.total_cost > 200:
            self.total_cost -= 20
        
        if self.selected_plan == 'Premium':
            self.total_cost *= 1.15  # Apply 15% surcharge for premium membership features
        
        return self.total_cost
  
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

