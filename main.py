class GymMembership:
    def isAvailable(self, membership):
        if membership == None or membership not in self.membership_plans: 
            raise ValueError("Membership not available")
        return True
    
        
