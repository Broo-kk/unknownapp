# Constants
TUITION_PER_CREDIT = 1000  # You can adjust this value based on the Java constant

class BillingSystem:
    def __init__(self, students_dict, courses_dict):
        self.students = students_dict
        self.courses = courses_dict

    def calculate_tuition(self, student_id):
        """
        Calculates the total tuition for a student based on enrolled credits.
        Returns -1.0 if the student is not found.
        """
        student = self.students.get(student_id)
        
        if student is None:
            return -1.0
            
        total_credits = 0
        # Iterate through student's enrolled course codes
        for code in student.get('enrolled_courses', []):
            course = self.courses.get(code)
            if course:
                total_credits += course.get('credits', 0)
        
        return float(total_credits * TUITION_PER_CREDIT)

# Example Usage/Mock Data for testing
if __name__ == "__main__":
    # Mock database
    mock_courses = {
        "ICT101": {"credits": 3},
        "ICT102": {"credits": 4}
    }
    mock_students = {
        "6688001": {"enrolled_courses": ["ICT101", "ICT102"]}
    }

    billing = BillingSystem(mock_students, mock_courses)
    
    # Test Use Case
    sid = "6688001"
    result = billing.calculate_tuition(sid)
    print(f"Billing Summary for Student {sid}: {result} Baht")
