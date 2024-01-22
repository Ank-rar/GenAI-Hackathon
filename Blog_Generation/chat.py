import requests
import json

#OPENROUTER_API_KEY = '''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'''
OPENROUTER_API_KEY = '''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'''


def get_response(query):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            # "HTTP-Referer": f"{YOUR_SITE_URL}", # Optional, for including your app on openrouter.ai rankings.
            # "X-Title": f"{YOUR_APP_NAME}", # Optional. Shows in rankings on openrouter.ai.
        },
        data=json.dumps({
            "model": "mistralai/mixtral-8x7b-instruct", # Optional
            "messages": [
            {"role": "user", "content": query}
            ]
        })
    )


    try:
        return response.json()['choices'][0]['message']['content']
    except KeyError:
        return response.json()['error']['message']


# print(get_response("Write a poem on going on a trip."))