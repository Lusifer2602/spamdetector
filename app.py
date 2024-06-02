from flask import Flask, request, render_template
import os


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        keywords = ["free", "discount", "limited time offer", "money back guarantee",  "make money", "win", "prize", "sale", "offer", "weight loss", "debt",  "refinance", "investment", "earn", "million", "billion", "lottery", "Viagra", "Cialis", "pills", "online pharmacy", "income", "opt-out", "multi-level marketing", "mlm", "weight loss", "diet", "body enhancement", "enlargement",  "investment opportunity", "herbal", "supplement", "lose weight fast", "no credit check",  "meet singles", "singles in your area", "meet hot girls", "earn extra cash", "lowest price",  "risk-free", "satisfaction guaranteed", "act fast", "money-making", "money-making opportunity",  "performance", "enhancement", "money-making", "income", "extra income", "earn money", "free trial", "meet girls", "meet women", "lose weight", "anti-aging", "live longer", "stop aging", "fast cash", "limited time", "no catch", "call now", "claim", "guarantee", "no obligation", "easy money", "free membership", "winner", "lowest mortgage rates", "lowest insurance rates", "lowest prices", "lowest interest rates", "no hidden costs", "buy now", "earn cash", "exclusive deal", "home business", "increase sales", "no fees", "no investment", "no purchase necessary", "reverses aging", "stop hair loss", "cash bonus", "cheap", "free consultation", "free gift", "free hosting", "free installation", "free investment", "free membership", "free trial", "lifetime", "mass email", "one hundred per cent free", "online marketing", "print form home", "pure profit", "save big money", "serious cash", "talks about hidden charges", "unsecured credit", "unsecured debt"]

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
