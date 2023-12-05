from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = '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'


def generate_lesson_plan(prompt):
    # Use GPT-3.5 Turbo to generate a lesson plan based on the prompt
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=300  # Adjust as needed
    )

    generated_plan = response['choices'][0]['text']
    return generated_plan


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_lesson_plan', methods=['POST'])
def generate_lesson_plan_route():
    user_prompt = request.form['user_prompt']

    # Use the user prompt to generate a lesson plan
    generated_plan = generate_lesson_plan(user_prompt)

    return render_template('index.html', user_prompt=user_prompt, generated_plan=generated_plan)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
