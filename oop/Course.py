class Course:
    def __init__(self, course_name, course_duration, *books):
        self.course_name = course_name
        self.course_duration = course_duration
        self.books = [self.Book(book) for book in books]
    
    def showDetails(self):
        print(f"Course Name: {self.course_name}")
        print(f"Course Duration: {self.course_duration}")
        print("Suggested Books: ")
        for i, book in enumerate(self.books):
            print(f"{i + 1}. {book}")
    class Book:
        def __init__(self, title):
            self.title = title
        
        def __str__(self) -> str:
            return self.title

c1 = Course('Python',10, 'Learn Python', 'Python for Data Science', 'Python for Beginners', 'Python OOP', 'DSA in Python')
c1.showDetails()