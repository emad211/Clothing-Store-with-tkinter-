فروشگاه پوشاک (Clothing Store)
این پروژه یک برنامه مدیریت فروشگاه پوشاک ساده است که با استفاده از زبان برنامه‌نویسی پایتون و کتابخانه Tkinter ساخته شده است. این برنامه به مدیر فروشگاه اجازه می‌دهد تا محصولات را اضافه، ویرایش، حذف و مشاهده کند. اطلاعات محصولات شامل آیدی، نام، قیمت، تعداد، رنگ، سایز و تصویر محصول می‌باشد.

ویژگی‌ها
افزودن محصول جدید
ویرایش اطلاعات محصول
حذف محصول
مشاهده لیست محصولات با امکان جستجو بر اساس آیدی، نام و قیمت
نمایش اطلاعات محصول همراه با تصویر، رنگ و سایز
نصب و راه‌اندازی
ابتدا مخزن را کلون کنید:

bash
Copy code
git clone https://github.com/username/clothing-store.git
cd clothing-store
کتابخانه‌های مورد نیاز را نصب کنید:

bash
Copy code
pip install pillow
فایل database.py را برای ایجاد پایگاه داده اجرا کنید:

bash
Copy code
python database.py
برنامه اصلی را اجرا کنید:

bash
Copy code
python app.py
فایل‌ها
database.py: شامل توابعی برای مدیریت پایگاه داده SQLite.
app.py: شامل رابط کاربری و منطق برنامه برای مدیریت محصولات.
زبان‌ها و ابزارهای استفاده شده
Python
Tkinter
SQLite
Pillow

Clothing Store
This project is a simple clothing store management application built with Python and the Tkinter library. The application allows the store manager to add, edit, delete, and view products. Product information includes ID, name, price, quantity, color, size, and product image.

Features
Add new product
Edit product information
Delete product
View product list with search functionality by ID, name, and price
Display product information with image, color, and size
Installation and Setup
Clone the repository:

bash
Copy code
git clone https://github.com/username/clothing-store.git
cd clothing-store
Install the required libraries:

bash
Copy code
pip install pillow
Run the database.py file to create the database:

bash
Copy code
python database.py
Run the main application:

bash
Copy code
python app.py
Files
database.py: Contains functions to manage the SQLite database.
app.py: Contains the user interface and logic for managing products.
Technologies and Tools Used
Python
Tkinter
SQLite
Pillow
