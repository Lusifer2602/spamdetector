import tkinter as tk
from tkinter import filedialog

def scan_text_file():
    file_name = file_entry.get()
    keywords = ["free", "discount", "limited time offer", "act now", "urgent", "money back guarantee", 
    "make money", "win", "prize", "click here", "call now", "order now", "amazing", "opportunity", 
    "cash", "bonus", "sale", "offer", "unbeatable", "weight loss", "get rid of", "credit", "card", 
    "debt", "mortgage", "refinance", "investment", "earn", "million", "billion", "lottery", "viagra", 
    "cialis", "pills", "pharmacy", "online pharmacy", "prescription", "medicine", "insurance", "guaranteed",
    "income", "work from home", "online job", "unsubscribe", "opt-out", "click below", "visit our website", 
    "multi-level marketing", "mlm", "weight loss", "diet", "body enhancement", "enlargement", 
    "investment opportunity", "herbal", "supplement", "lose weight fast", "miracle", "no credit check", 
    "meet singles", "singles in your area", "viagra", "meet hot girls", "earn extra cash", "lowest price", 
    "risk-free", "satisfaction guaranteed", "act fast", "money-making", "money-making opportunity", 
    "performance", "enhancement", "money-making", "income", "extra income", "earn money", "free trial", 
    "privacy", "meet girls", "meet women", "lose weight", "anti-aging", "live longer", "stop aging", 
    "fast cash", "limited time", "no catch", "call now", "claim", "guarantee", "winner", "no obligation", 
    "easy money", "free membership", "winner", "lowest mortgage rates", "lowest insurance rates", 
    "lowest prices", "lowest interest rates", "no hidden costs", "apply now", "buy now", "earn cash", 
    "exclusive deal", "home business", "increase sales", "no fees", "no investment", "no purchase necessary", 
    "refund", "reverses aging", "stop hair loss", "your family", "act today", "be your own boss", 
    "believe in yourself", "cash bonus", "cheap", "free consultation", "free gift", "free hosting", 
    "free installation", "free investment", "free membership", "free trial", "lifetime", "mass email", 
    "one hundred percent free", "online marketing", "print form home", "pure profit", "save big money", 
    "serious cash", "starting from scratch", "success", "talks about hidden charges", "terms and conditions", 
    "unsecured credit", "unsecured debt", "urgent notice", "winner"]

    found_keywords = []
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            for kw in keywords:
                if kw.lower() in text.lower():
                    found_keywords.append(kw)

            result_label.config(text=f"Matching Keywords found in the text:, {len(found_keywords)}")
            if len(found_keywords) >= 5:
                spam_label.config(text="This Email / document is likely a spam")
            else:
                spam_label.config(text="This Email / document is not a spam")
    except FileNotFoundError:
        result_label.config(text=f"Error: File '{file_name}' not found.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

root = tk.Tk()
root.title("TEST AWS")
root.geometry("425x262")

background_image = tk.PhotoImage(file="bg.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

file_label = tk.Label(root, text="Select Text File:")
file_label.grid(row=2, column=1, padx=5, pady=5)
file_entry = tk.Entry(root, width=40)
file_entry.grid(row=4, column=2, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=2, column=3, padx=5, pady=5)

scan_button = tk.Button(root, text="Scan File", command=scan_text_file)
scan_button.grid(row=6, column=1, columnspan=3, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=10, column=1, columnspan=5, padx=5, pady=5)

spam_label = tk.Label(root, text="")
spam_label.grid(row=12, column=1, columnspan=5, padx=5, pady=5)

root.mainloop()
