from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#sample chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "help" in user_input:
        return "I'm here to help! What do you need assistance with?"
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How can I assist you?"
    elif "what is your name" in user_input:
        return "I am a chatbot created to assist you."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "weather" in user_input:
        return "I can't check the weather, but you can look it up online!"
    elif "news" in user_input:
        return "I don't have news updates, but you can check your favorite news site!"
    elif "joke" in user_input:
        return "Why did the scarecrow win an award? Because he was outstanding in his field!"
    elif "favorite color" in user_input:
        return "I don't have a favorite color, but I think blue is nice!"
    elif "tell me something" in user_input:
        return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!"
    else:
        return "Sorry, I didn't understand that!"

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chatbot_response(user_input) 
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)              