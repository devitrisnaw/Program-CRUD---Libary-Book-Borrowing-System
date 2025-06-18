# CRUD Program---Library Book Borrowing System
- This is a simple command-line application built using Python for managing book borrowing and returning in a library environment. The system is designed to assist library staff with daily operations and ensure accurate data handling.

# Benefits:
- Develop a computer-based system to efficiently manage book borrowing and returns.
- Simplify the search and availability checking of books.
- Improve accuracy in borrower data records.
- Provide basic reporting related to book loans.
- Reduce the workload on library staff.
- 
### Target User:
- Staff Library
- 
# Features:
- **Create**
- Add new borrower data when borrowing books.
- **Read**
- Display full list of available books.
- View borrower records.
- Search books by title or author.
- **Update**
- Edit book information (title, author, category, stock).
- **Delete**
- Remove a book by its `id_buku`.
- **Utilities**
- Borrow a book with automatic return date (10 days).
- Prevent duplicate borrowing of the same book by one user.
- Return a book and check for overdue days.
- Date input validation (`DD-MM-YYYY` format).

# Installation
### 1. Clone the repository
git clone https://github.com/yourusername/CRUDProgram-Library_Borrowing_System.git
cd CRUDProgram-Library_Borrowing_System
pip install -r requirements.txt

### Install dependencies
pip install tabulate

# Usage
### Run the application:
python main.py
