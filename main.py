from flask import Flask, render_template, request, jsonify


app = Flask(
  __name__,
  template_folder='.',
  static_folder='.'
)

@app.route('/')
def index():
    print("in the index")
    return render_template('Chatbot.html')

@app.route('/submit', methods=['POST'])
def submit():
    print("submit")
    data = request.get_json()
    message = data.get('message')

    # Process the message and generate a response
    if not message:
        response = "Hello! How may I assist you today?"
    else:
        response = f"You sent: {message}"  # Replace this with your actual response logic

    # Log the received message
    print(f"Received message: {message}")

    # Return the response in JSON format
    return jsonify({'response': response})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

