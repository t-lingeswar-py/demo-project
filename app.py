from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simulated AI feedback function
def get_ai_feedback(answer):
    if not answer.strip():
        return "Please provide an answer to get feedback."
    feedback = "<strong>AI Feedback:</strong><ul>"
    if len(answer) < 50:
        feedback += "<li>Your answer is a bit short. Try giving more detail or examples.</li>"
    if any(word in answer.lower() for word in ["confident", "motivated", "team", "learn"]):
        feedback += "<li>Great use of positive keywords!</li>"
    if any(word in answer.lower() for word in ["um", "uh", "like"]):
        feedback += "<li>Try to avoid filler words for a stronger impression.</li>"
    feedback += "<li>Speak clearly and structure your answer logically (e.g., background, skills, motivation).</li>"
    feedback += "</ul>"
    return feedback

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/api/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    answer = data.get('answer', '')
    result = get_ai_feedback(answer)
    return jsonify({'feedback': result})

if __name__ == '__main__':
    app.run(debug=True)
