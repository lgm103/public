#simple openAI queries
#by LM



from openai import OpenAI
import os


client=OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

#completion = client.completions.create(
#	model="gpt-4o-mini",
#	prompt="Write a short story about a troll.",
#	max_tokens=100,
#	temperature=2,
#)

#print(completion.choices[0].text)


stream= client.chat.completions.create(
	model = "gpt-4o-mini",
	messages = [{
			"role": "user", 
		     	"content": "Generate python code to draw a pyramid",
			"temperature" : ".2"
		}],
	stream=True,
)

for chunk in stream:
	if chunk.choices[0].delta.content is not None:
		print(chunk.choices[0].delta.content, end = "")

print("\n")
