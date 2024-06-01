from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
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
                    "lowest prices", "lowest interest rates", "no hidden costs", "applynow", "buy now", "earn cash", 
                    "exclusive deal", "home business", "increase sales", "no fees", "no investment", "no purchase necessary", 
                    "refund", "reverses aging", "stop hair loss", "your family", "act today", "be your own boss", 
                    "believe in yourself", "cash bonus", "cheap", "free consultation", "free gift", "free hosting", 
                    "free installation", "free investment", "free membership", "free trial", "lifetime", "mass email", 
                    "one hundred percent free", "online marketing", "print form home", "pure profit", "save big money", 
                    "serious cash", "starting from scratch", "success", "talks about hidden charges", "terms and conditions",
                    "unsecured credit", "unsecured debt", "urgent notice", "winner"]

        found_keywords = []
        try:
            text = file.read().decode('utf-8')
            for kw in keywords:
                if kw.lower() in text.lower():
                    found_keywords.append(kw)

            file.save(os.path.join('uploads', file.filename))
            return render_template('result.html', found_keywords=found_keywords, num_keywords=len(found_keywords))
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)