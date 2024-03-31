import openai
import gradio

openai.api_key ="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"
messages = [{"role": "system", "content": "You are a Physiotherapy experts also known as Extended Scope Practitioners (ESPs)"}]

def CustomChatGPT(user_input):
    try:
        messages.append({"role": "user", "content": user_input})
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=150
        )
        ChatGPT_reply = response.choices[0].text.strip()
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    except Exception as e:
        return str(e)

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Deepak physiotherapy specialist")

demo.launch(share=True)

