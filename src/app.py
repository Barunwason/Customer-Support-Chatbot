from flask import Flask,render_template,request
from customer_support_automation.main import run
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    if request.method == 'POST':
        name = request.form['name']
        profession = request.form['profession']
        query = request.form['query']
        
        inputs = {
            "customer": profession,
            "person": name,
            "inquiry": query
        }
        
        response = markdown.markdown(run(inputs))
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Return JUST the response text for AJAX
            return response
        # Return full template for normal requests
        return render_template('index.html', response=response)
    
    # GET request - return empty form
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)