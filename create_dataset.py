import pandas as pd

# Load both datasets
fake = pd.read_csv("/kaggle/input/isot-fake-news-dataset/Fake.csv")
true = pd.read_csv("/kaggle/input/isot-fake-news-dataset/True.csv")

# Add labels
fake["label"] = 0
true["label"] = 1

# Combine and shuffle
df = pd.concat([fake, true], axis=0)
df = df.sample(frac=1).reset_index(drop=True)

# Save final dataset
df.to_csv("fake_news_dataset.csv", index=False)

print("✅ Dataset saved as fake_news_dataset.csv")
