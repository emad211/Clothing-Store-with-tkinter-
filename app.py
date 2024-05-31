import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from PIL import Image, ImageTk
import database

database.create_table()

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("پنل مدیریت فروشگاه پوشاک مریم")
        self.root.geometry("800x600")

        self.image_path = None

        self.create_menu()
        self.create_main_frame()
    
    def create_menu(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        self.product_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="محصولات", menu=self.product_menu)
        self.product_menu.add_command(label="مشاهده محصولات", command=self.show_product_view)
        self.product_menu.add_command(label="اضافه کردن محصول", command=self.show_add_product_view)
        self.product_menu.add_command(label="ویرایش محصول", command=self.show_edit_product_prompt)
        self.product_menu.add_command(label="حذف محصول", command=self.show_delete_product_prompt)
    
    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=1)
    
    def show_product_view(self):
        self.clear_frame()
        self.create_product_view()
    
    def create_product_view(self):
        search_frame = tk.Frame(self.main_frame)
        search_frame.pack(pady=10, anchor='e')

        tk.Label(search_frame, text="آیدی ").pack(side=tk.RIGHT, padx=5)
        self.search_id_entry = tk.Entry(search_frame)
        self.search_id_entry.pack(side=tk.RIGHT, padx=5)

        tk.Label(search_frame, text="نام").pack(side=tk.RIGHT, padx=5)
        self.search_name_entry = tk.Entry(search_frame)
        self.search_name_entry.pack(side=tk.RIGHT, padx=5)

        tk.Label(search_frame, text="قیمت از").pack(side=tk.RIGHT, padx=5)
        self.search_price_min_entry = tk.Entry(search_frame)
        self.search_price_min_entry.pack(side=tk.RIGHT, padx=5)
        tk.Label(search_frame, text="تا").pack(side=tk.RIGHT, padx=5)
        self.search_price_max_entry = tk.Entry(search_frame)
        self.search_price_max_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(search_frame, text="جستجو", command=self.search_product).pack(side=tk.RIGHT, padx=5)

        self.products_list_frame = tk.Frame(self.main_frame)
        self.products_list_frame.pack(fill=tk.BOTH, expand=1)
        self.view_products()
    
    def search_product(self):
        product_id = self.search_id_entry.get()
        product_name = self.search_name_entry.get()
        price_min = self.search_price_min_entry.get()
        price_max = self.search_price_max_entry.get()

        query = "SELECT * FROM products WHERE 1=1"
        params = []

        if product_id:
            query += " AND id=?"
            params.append(product_id)

        if product_name:
            query += " AND name LIKE ?"
            params.append(f"%{product_name}%")

        if price_min:
            try:
                price_min = float(price_min)
                query += " AND price >= ?"
                params.append(price_min)
            except ValueError:
                messagebox.showerror("خطا", "قیمت باید عدد باشد.")
                return

        if price_max:
            try:
                price_max = float(price_max)
                query += " AND price <= ?"
                params.append(price_max)
            except ValueError:
                messagebox.showerror("خطا", "قیمت باید عدد باشد.")
                return

        connection = database.create_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)
        products = cursor.fetchall()
        connection.close()

        if products:
            self.clear_products_list()
            for product in products:
                self.display_product(product)
        else:
            messagebox.showinfo("نتیجه جستجو", "محصولی با این مشخصات یافت نشد.")
    
    def clear_products_list(self):
        for widget in self.products_list_frame.winfo_children():
            widget.destroy()
    
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_add_product_view(self):
        self.clear_frame()
        self.add_product_frame = tk.Frame(self.main_frame)
        self.add_product_frame.pack(pady=20)

        tk.Label(self.add_product_frame, text="آیدی محصول:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.id_entry = tk.Entry(self.add_product_frame)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5, sticky='e')

        tk.Label(self.add_product_frame, text="نام محصول:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.name_entry = tk.Entry(self.add_product_frame)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky='e')

        tk.Label(self.add_product_frame, text="قیمت محصول:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.price_entry = tk.Entry(self.add_product_frame)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5, sticky='e')

        tk.Label(self.add_product_frame, text="تعداد محصول:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.quantity_entry = tk.Entry(self.add_product_frame)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=5, sticky='e')

        tk.Label(self.add_product_frame, text="رنگ محصول:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.color_entry = tk.Entry(self.add_product_frame)
        self.color_entry.grid(row=4, column=1, padx=10, pady=5, sticky='e')

        tk.Label(self.add_product_frame, text="سایز محصول:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
        self.size_entry = tk.Entry(self.add_product_frame)
        self.size_entry.grid(row=5, column=1, padx=10, pady=5, sticky='e')

        tk.Button(self.add_product_frame, text="انتخاب تصویر محصول", command=self.upload_image).grid(row=6, column=0, columnspan=2, pady=10)

        tk.Button(self.add_product_frame, text="اضافه کردن محصول", command=self.add_product).grid(row=7, column=0, columnspan=2, pady=20)
    
    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    
    def show_edit_product_prompt(self):
        product_id = simpledialog.askinteger("ورودی", "آیدی محصول برای ویرایش را وارد کنید:")
        if product_id:
            self.show_edit_product_view(product_id=product_id)
    
    def show_edit_product_view(self, event=None, product_id=None):
        if event:
            selected_product = self.products_listbox.get(self.products_listbox.curselection())
            product_id = int(selected_product.split(' - ')[0])
        elif product_id is None:
            return

        product = database.get_product_by_id(product_id)
        if product:
            self.clear_frame()
            self.edit_product_frame = tk.Frame(self.main_frame)
            self.edit_product_frame.pack(pady=20)

            tk.Label(self.edit_product_frame, text="نام محصول:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
            self.name_entry = tk.Entry(self.edit_product_frame)
            self.name_entry.insert(0, product[1])
            self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='e')

            tk.Label(self.edit_product_frame, text="قیمت محصول:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
            self.price_entry = tk.Entry(self.edit_product_frame)
            self.price_entry.insert(0, product[2])
            self.price_entry.grid(row=1, column=1, padx=10, pady=5, sticky='e')

            tk.Label(self.edit_product_frame, text="تعداد محصول:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
            self.quantity_entry = tk.Entry(self.edit_product_frame)
            self.quantity_entry.insert(0, product[3])
            self.quantity_entry.grid(row=2, column=1, padx=10, pady=5, sticky='e')

            tk.Label(self.edit_product_frame, text="رنگ محصول:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
            self.color_entry = tk.Entry(self.edit_product_frame)
            self.color_entry.insert(0, product[5])
            self.color_entry.grid(row=3, column=1, padx=10, pady=5, sticky='e')

            tk.Label(self.edit_product_frame, text="سایز محصول:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
            self.size_entry = tk.Entry(self.edit_product_frame)
            self.size_entry.insert(0, product[6])
            self.size_entry.grid(row=4, column=1, padx=10, pady=5, sticky='e')

            tk.Button(self.edit_product_frame, text="انتخاب تصویر جدید", command=self.upload_image).grid(row=5, column=0, columnspan=2, pady=10)

            tk.Button(self.edit_product_frame, text="به روز رسانی محصول", command=lambda: self.edit_product(product_id)).grid(row=6, column=0, columnspan=2, pady=20)
    
    def show_delete_product_prompt(self):
        product_id = simpledialog.askinteger("ورودی", "آیدی محصول برای حذف را وارد کنید:")
        if product_id:
            self.delete_product(product_id)
    
    def display_product(self, product):
        product_frame = tk.Frame(self.products_list_frame, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        product_frame.pack(pady=10, fill=tk.X)

        if product[4]:
            img = Image.open(product[4])
            img = img.resize((100, 100), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(product_frame, image=img)
            img_label.image = img
            img_label.pack(side=tk.LEFT, padx=10)

        info_frame = tk.Frame(product_frame)
        info_frame.pack(side=tk.LEFT)

        tk.Label(info_frame, text=f"آیدی محصول: {product[0]}").pack(anchor='w')
        tk.Label(info_frame, text=f"نام محصول: {product[1]}").pack(anchor='w')
        tk.Label(info_frame, text=f"قیمت: {product[2]} تومان").pack(anchor='w')
        tk.Label(info_frame, text=f"موجودی: {product[3]} عدد").pack(anchor='w')
        tk.Label(info_frame, text=f"رنگ: {product[5]}").pack(anchor='w')
        tk.Label(info_frame, text=f"سایز: {product[6]}").pack(anchor='w')

    def view_products(self):
        products = database.get_products()
        self.clear_products_list()
        for product in products:
            self.display_product(product)
    
    def add_product(self):
        product_id = self.id_entry.get()
        name = self.name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        color = self.color_entry.get()
        size = self.size_entry.get()
        if product_id and name and price and quantity and self.image_path and color and size:
            try:
                product_id = int(product_id)
                price = float(price)
                quantity = int(quantity)
                database.add_product(product_id, name, price, quantity, self.image_path, color, size)
                self.show_product_view()
            except ValueError:
                messagebox.showerror("خطا", "ورودی نامعتبر برای آیدی، قیمت یا تعداد")
        else:
            messagebox.showerror("خطا", "تمامی فیلدها و انتخاب تصویر باید پر شوند")
    
    def edit_product(self, product_id):
        name = self.name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        color = self.color_entry.get()
        size = self.size_entry.get()
        if name and price and quantity and self.image_path and color and size:
            try:
                price = float(price)
                quantity = int(quantity)
                database.update_product(product_id, name, price, quantity, self.image_path, color, size)
                self.show_product_view()
            except ValueError:
                messagebox.showerror("خطا", "ورودی نامعتبر برای قیمت یا تعداد")
        else:
            messagebox.showerror("خطا", "تمامی فیلدها و انتخاب تصویر باید پر شوند")
    
    def delete_product(self, product_id):
        product = database.get_product_by_id(product_id)
        if product:
            if messagebox.askyesno("تأیید", f"آیا مطمئنید که می‌خواهید {product[1]} را حذف کنید؟"):
                database.delete_product(product_id)
                self.show_product_view()
        else:
            messagebox.showerror("خطا", "محصول پیدا نشد")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminPanel(root)
    root.mainloop()
