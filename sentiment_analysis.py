from textblob import TextBlob
from tkinter import *

root = Tk()
root.title("Sentiment Analysis")
root.geometry("600x400")

Label(root, text="Sentiment Analysis",
      font=("Arial",16,"bold")).pack(pady=10)

Label(root, text="Enter Review").pack()

review = Text(root, height=8, width=60)
review.pack()

result = Label(root, text="", font=("Arial",14))
result.pack(pady=20)

def analyze():
    text = review.get("1.0", END)

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    result.config(text="Sentiment: " + sentiment)

Button(root,
       text="Analyze",
       command=analyze,
       bg="green",
       fg="white").pack(pady=10)

root.mainloop()
