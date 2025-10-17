# ai_chatbot.py
import openai

openai.api_key = "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"  # 🔑 Replace with your key

print("🤖 PyBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("🤖 PyBot: Goodbye! Have a great day! 😊")
        break

    try:
        # New OpenAI API usage (>=1.0.0)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are PyBot, a friendly AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        reply = response.choices[0].message.content
        print("🤖 PyBot:", reply)

    except Exception as e:
        print("⚠️ Error:", e)
