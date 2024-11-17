import openai
import tweepy

# OpenAI API Setup
openai.api_key = "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"

# Twitter API Setup
auth = tweepy.OAuth1UserHandler(
    "yOmYSwuxbec6KeqsrhN0DrtAA", 
    "I2wM7BydfPrGbhf8uVnvjvpjhqlIiAd9PtVYue9JY5nqVEMScv", 
    "1539948411880968196-Dn75xWTHByPoJX0BpXOwCnFv957vwV", 
    "Ram8hVp6F4LKQwHuArFM2odovFQeKmfl5XLSWta2BdIOI"
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
