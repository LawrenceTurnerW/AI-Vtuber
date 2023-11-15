from openai import OpenAI
import config
key = config.OPENAI_KEY

client = OpenAI(api_key=key)

class OpenAIChat:
	def __init__(self):
		self.system_prompt = "こんにちは"

	def _create_text(self,role,text):
		return {
			"role":role,
			"content":text
		}

	def create_chat(self,input_text):
		agent_text = self._create_text("system",self.system_prompt)
		user_text = self._create_text("user",input_text)
		messages = [
			agent_text,
			user_text
		]

		res = client.chat.completions.create(
  			model="gpt-3.5-turbo",
  			messages = messages
			)
		
		return res.choices[0].message.content

if __name__ == "__main__":
	adapter = OpenAIChat()
	response_text = adapter.create_chat("こんにちは")
	print(response_text)