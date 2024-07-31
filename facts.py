#a simple webapp to retrieve random facts and display them in browser

import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fact(_):
	#clear the screen
	clear()
	put_html(
		'<p align="left">'
		'<h2></h2></p>')
	
	url = "https://uselessfacts.jsph.pl/random.json?language=en"
	response = requests.get(url)
	data = json.loads(response.text)
	useless_fact = data['text']
	style(put_text(useless_fact), 'color:blue; font-size: 30px')
	put_buttons(
		[dict(label='Get Fact', value = 'outline-success', color='outline-success')],
		onclick=get_fact
		)

if __name__ == '__main__':
	put_html(
		'<p align = "left"'>
		'<h2></h2></p>'
		)
	put_buttons(
		[dict(label='Get Fact', value = 'outline-success', color = 'outline-success')], 
		onclick=get_fact
		)
	hold()
