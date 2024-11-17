import openai
import tweepy

# OpenAI API Setup
openai.api_key = "YOUR_OPENAI_API_KEY"

# Twitter API Setup
auth = tweepy.OAuth1UserHandler(
    "SRyFFNFx5dovpvq2TOlZjrxlg", 
    "MTMZnzrbaBVoWGNtfY838HoBRjGIRUkrHErg10v9vgCUVV8k4z", 
    "1539948411880968196-Gd1wBNAI3xFNTnLzB8YjgvEaVpslh7", 
    "s1UvgzFjjPzqGcIHGuRg5RmxJW0dJgzNb7MOjpDCVVbxF"
)
api = tweepy.API(auth)

# Generate Content with ChatGPT
def generate_tweet(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=280,  # Ensure tweet length fits
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Post Tweet
def post_tweet(content):
    try:
        api.update_status(content)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Error posting tweet: {e}")

# Main
if __name__ == "__main__":
    prompt = "Create a motivational tweet for the day."
    tweet_content = generate_tweet(prompt)
    post_tweet(tweet_content)
