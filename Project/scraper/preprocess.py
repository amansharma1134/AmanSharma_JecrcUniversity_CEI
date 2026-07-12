import re

# Read the scraped text
with open("data/raw_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Remove extra spaces and blank lines
text = re.sub(r"\s+", " ", text).strip()

# Save cleaned text
with open("data/clean_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Data cleaned successfully!")
