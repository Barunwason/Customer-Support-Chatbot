from flask import Flask,render_template,request
from customer_support_automation.main import run
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    if request.method == 'POST':
        name=request.form['name']
        profession=request.form['profession']
        query = request.form['query']
        
        inputs = {
        "customer": profession,
        "person": name,
        "inquiry": query
        }
        run(inputs)

        with open("final_draft.md", "r") as file:
            response = file.read()
            response_lines = response.strip().split('\n')

    return render_template('index.html', response=response_lines)

if __name__ == '__main__':
    app.run(debug=True)