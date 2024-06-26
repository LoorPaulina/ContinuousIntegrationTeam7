class GymMembership:
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
