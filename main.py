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
