######################## TASK 1A ########################

class Member:
	def __init__(self, name: str, member_id):
		self.__name = name
		self.__member_id = member_id
		self.__borrowed_books = []

	# property with getter and setter
	@property
	def name(self) -> str:
		return self.__name

	@name.setter
	def name(self, new_name: str):
		if not isinstance(new_name, str):
			raise TypeError("Name must be a string")
		if new_name == "":
			raise ValueError("Name cannot be empty")
		self.__name = new_name

	# property with only getter
	@property
	def member_id(self):
		return self.__member_id

	# restrict access to borrowed_books (expose copy)
	@property
	def borrowed_books(self):
		# return immutable copy, prevent external modification
		return tuple(self.__borrowed_books)

	def borrow_book(self, book_name: str):
		if not isinstance(book_name, str) or book_name == "":
			raise ValueError("book_name must be a non-empty string")
		self.__borrowed_books.append(book_name)

	def return_book(self, book_name: str):
		try:
			self.__borrowed_books.remove(book_name)
		except ValueError:
			raise ValueError(f"Book '{book_name}' not found in borrowed books")

	def show_info(self):
		print(f"Member name: {self.__name}")
		if self.__borrowed_books:
			print("Borrowed books:")
			for b in self.__borrowed_books:
				print(f" - {b}")
		else:
			print("No borrowed books")


if __name__ == "__main__":
	# simple demonstration / tests
	m = Member("Thomas", 123)
	m.show_info()
	print()

	m.borrow_book("1984 de George Orwell")
	m.borrow_book("DANA-DMBOK")
	m.show_info()
	print()

	# test "security" of borrowed_books
	books = m.borrowed_books
	print(type(books), books) # should be tuple
	try:
		books += ("Some new book",)
		print("try external modification --> internal list:")
		m.show_info()
	except Exception as e:
		print("Could not modify borrowed_books externally:", e)

	m.return_book("1984 de George Orwell")
	print("return book")
	m.show_info()
	print()

	# test setter
	try:
		m.name = ""  # should raise
	except Exception as e:
		print("Name update prevented (successfully):", e)

######################## TASK 1B ########################
class Student:
	def __init__(self, name: str):
		if not isinstance(name, str) or name == "":
			raise ValueError("name must be a non-empty string")
		self.__name = name
		# grades stored privately as {subject: score}
		self.__grades = {}

	@property
	def name(self) -> str:
		return self.__name

	# return copy of grades (prevent modification)
	@property
	def grades(self):
		return dict(self.__grades)

	def add_grade(self, subject: str, score: float):
		if not isinstance(subject, str) or subject == "":
			raise ValueError("subject must be a non-empty string")
		if not (isinstance(score, (int, float))):
			raise TypeError("score must be a number between 0 and 100")
		if not (0 <= score <= 100):
			raise ValueError("score must be between 0 and 100")
		self.__grades[subject] = float(score)

	def calculate_average(self) -> float:
		if not self.__grades:
			return 0.0
		return sum(self.__grades.values()) / len(self.__grades)

	def get_info(self):
		avg = self.calculate_average()
		print(f"Student name: {self.__name}")
		print(f"Average score: {avg:.2f}")


if __name__ == "__main__":
	# Student demo/tests
	s = Student("Thomas")
	s.get_info()
	print()

	s.add_grade("Algorithm and Programming", 95)
	s.add_grade("Discrete Maths", 88.5)
	s.add_grade("Statistics", 86)
	print("added grades")
	s.get_info()
	print()

	print("Grades dict (external copy):", s.grades)
	try:
		s.add_grade("Science", 150)  # invalid score
	except Exception as e:
		print("Invalid grade rejected (successfully):", e)


