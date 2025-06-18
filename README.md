# CRUD Program---Library Book Borrowing System
- This is a simple command-line application built using Python for managing book borrowing and returning in a library environment. The system is designed to assist library staff with daily operations and ensure accurate data handling.

# Benefits:
- Develop a computer-based system to efficiently manage book borrowing and returns.
- Simplify the search and availability checking of books.
- Improve accuracy in borrower data records.
- Provide basic reporting related to book loans.
- Reduce the workload on library staff.
  
### Target User:
- Staff Library
  
# Features:
CREATE
- Add new borrower data when borrowing books.

READ
- Display full list of available books.
- View borrower records.
- Search books by title or author.

UPDATE
- Edit book information (title, author, category, stock).

DELETE
- Remove a book by its `id_buku`.

UTILITIES
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

# Data Model
### Book Data (daftar_buku)
- id_buku (String, Primary Key): Unique identifier for each book (e.g., "B1").
- judul (String): Title of the book.
- penulis (String): Author of the book.
- kategori (String): Category or genre of the book (e.g., Novel, Motivasi, Biografi).
- stok (Integer): Number of available copies in the library.
### Borrower Data (data_peminjam)
- ID (Integer, Primary Key): Unique identifier for each borrower transaction.
- Nama Peminjam (String): Name of the person borrowing the book.
- Judul Buku (String): Title of the book being borrowed.
- Tanggal Pinjam (Date, format: DD-MM-YYYY): The date the book was borrowed.
- Tanggal Kembali (Date, format: DD-MM-YYYY): The due date for returning the book (10 days after borrowing).
