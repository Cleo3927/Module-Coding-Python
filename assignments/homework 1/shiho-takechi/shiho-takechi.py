# ==============================================================================
# 1. DATA AND CONTEXT
# ==============================================================================
#Data Source　Text data from eBay listings obtained by searching for “Lalka.”
#Reason: This dataset includes mixed information such as prices, seller ratings, and product names. Therefore, it was
# ideal for testing both regular expression extraction and NLP techniques like noise removal and keyword identification.
text = """
Sort: Best Match

Shop on eBay
Shop on eBay
Brand New
$20.00
or Best Offer
Shop on eBay
Shop on eBay
Brand New
$20.00
or Best Offer
Polish classic book "Lalka" by Boleslaw Prus, published in Krakow, PL 1999...
Find similar items
See all the items on eBay that match this style

Polish classic book "Lalka" by Boleslaw Prus, published in Krakow, PL 1999...Opens in a new window or tab
$70.00
or Best Offer
Shipping not specified
Located in United States
sylviajd 100% positive (45)
Sylvain Lilli Lalka Julian Kalinowski Severine OOAK RARE!
Sylvain Lilli Lalka Julian Kalinowski Severine OOAK RARE!Opens in a new window or tab
Pre-Owned
$600.00
Buy It Now
+$40.00 delivery
Located in South Korea
poplife13 98.1% positive (474)
Black Lalka Doll  Bild Lilli replica by Julian Kalinowski 
Black Lalka Doll Bild Lilli replica by Julian KalinowskiOpens in a new window or tab
Pre-Owned
$402.81
or Best Offer
+$29.66 shipping estimate
Located in United Kingdom
17 watchers
Customs services and international tracking provided
newshoes1992 100% positive (402)
Sylvain Lilli Lalka Julian Kalinowski Severine OOAK RARE!
Sylvain Lilli Lalka Julian Kalinowski Severine OOAK RARE!Opens in a new window or tab
Pre-Owned
$600.00
Buy It Now
+$40.00 delivery
Located in South Korea
poplife13 98.1% positive (474)
SOLANGE Lalka SEVINYL CAPRICE OOAK FASHION Doll Julian Kalinowski RARE barbie
SOLANGE Lalka SEVINYL CAPRICE OOAK FASHION Doll Julian Kalinowski RARE barbieOpens in a new window or tab
Pre-Owned
$330.00
Buy It Now
+$12.00 delivery
Located in Mexico
14 watchers
bob_drake 99.6% positive (11.5K)
Sylvain RARE Wigged Sylvain Lilli Lalka Julian Kalinowski Severine OOAK (READ)
Sylvain RARE Wigged Sylvain Lilli Lalka Julian Kalinowski Severine OOAK (READ)Opens in a new window or tab
Pre-Owned
$550.00
Buy It Now
+$40.00 delivery
Located in South Korea
poplife13 98.1% positive (474)
Very Rare Picture Lilli Lalka Doll First Model Sylvain Severine

Very Rare Picture Lilli Lalka Doll First Model Sylvain SeverineOpens in a new window or tab
Pre-Owned
$501.17
or Best Offer
+$46.62 delivery
Located in France
48 watchers
rosedevenise 100% positive (1.4K)
Very Rare Séverine Doll Picture Lilli Lalka 

Very Rare Séverine Doll Picture Lilli LalkaOpens in a new window or tab
Brand New
$571.10
or Best Offer
+$46.62 delivery
Located in France
35 watchers
rosedevenise 100% positive (1.4K)
Severine Lalka Bild Lilli Sylvain Julian Kalinowski ooak Doll RARE (READ)
Severine Lalka Bild Lilli Sylvain Julian Kalinowski ooak Doll RARE (READ)Opens in a new window or tab
Pre-Owned
$550.00
Buy It Now
+$40.00 delivery
Located in South Korea
17 watchers
poplife13 98.1% positive (474)
Severine Lalka Bild Lilli Sylvain Julian Kalinowski ooak Doll RARE (READ)
Severine Lalka Bild Lilli Sylvain Julian Kalinowski ooak Doll RARE (READ)Opens in a new window or tab
Pre-Owned
$600.00
Buy It Now
+$40.00 delivery
Located in South Korea
14 watchers
poplife13 98.1% positive (474)
Severine Lalka Bild Lilli Sylvain Julian Kalinowski ooak Doll RARE (READ)
Severine Lalka Bild Lilli Sylvain Julian Kalinowski ooak Doll RARE (READ)Opens in a new window or tab
Pre-Owned
$650.00
Buy It Now
+$35.00 delivery
Located in South Korea
15 watchers
poplife13 98.1% positive (474)
Very Rare Rachel Doll By Liz (not Solange) Lilli Lalka

Very Rare Rachel Doll By Liz (not Solange) Lilli LalkaOpens in a new window or tab
Pre-Owned
$524.48
or Best Offer
+$46.62 delivery
Located in France
13 watchers
rosedevenise 100% positive (1.4K)
Tretchikoff Severine Lalka Bild Lilli Sylvain Julian Kalinowski ooak Doll (READ)
Tretchikoff Severine Lalka Bild Lilli Sylvain Julian Kalinowski ooak Doll (READ)Opens in a new window or tab
Pre-Owned
$550.00
Buy It Now
+$40.00 delivery
Located in South Korea
54 watchers
poplife13 98.1% positive (474)
Bild Lilli Interest RARE AA STELLA DOLL - Julian Kalinowski Lilli Lalka
Bild Lilli Interest RARE AA STELLA DOLL - Julian Kalinowski Lilli LalkaOpens in a new window or tab
OOAK Artist
Pre-Owned
$425.00
or Best Offer
+$41.94 delivery
Located in United States
35 watchers
toxicwaistbydeadjohnny 100% positive (455)
Vintage Polish Folk Lalki Lalka Ludowa Handmade Doll
Vintage Polish Folk Lalki Lalka Ludowa Handmade DollOpens in a new window or tab
Pre-Owned
$2.50
0 bids · Time left2d 23h left (Thu, 07:46 PM)
+$28.44 delivery
Located in United States
thevintagevaultduo 99.5% positive (277)
WAKA Straw Hat Julian Kalinowski had made in London for his Bild Lilli Dolls
WAKA Straw Hat Julian Kalinowski had made in London for his Bild Lilli DollsOpens in a new window or tab
Brand New
$150.00
Buy It Now
+$31.00 delivery
Located in United States
13 watchers
annabelly1 100% positive (7K)
Vintage  Polish Doll Lalka Kurpiaaka Wedding doll from Poland
Vintage Polish Doll Lalka Kurpiaaka Wedding doll from PolandOpens in a new window or tab
Pre-Owned
$5.00
1 bid · Time left2d 21h left (Thu, 06:24 PM)
+$27.24 delivery
Located in United States
beckie701 100% positive (841)
Little Miss Lolita Lalka Doll
Little Miss Lolita Lalka DollOpens in a new window or tab
Pre-Owned
$550.00
or Best Offer
+$49.88 delivery
Located in United States
steviebssteven 100% positive (3.1K)
LALKA HISTORYCZ PULASKI HANDMADE 10”
LALKA HISTORYCZ PULASKI HANDMADE 10”Opens in a new window or tab
Pre-Owned
$199.99
or Best Offer
+$36.76 delivery
Located in United States
monroereading 99.4% positive (11.6K)
194735255603 Lalka Barbie Fashionistas w stroju cheerleaderki Mattel
194735255603 Lalka Barbie Fashionistas w stroju cheerleaderki MattelOpens in a new window or tab
Brand New
$20.14
or Best Offer
+$18.53 shipping estimate
Located in United Kingdom
Customs services and international tracking provided
*welsh_girl* 100% positive (307)
LALKA HISTORYCZ PULASKI HANDMADE 10”   FB21
LALKA HISTORYCZ PULASKI HANDMADE 10” FB21Opens in a new window or tab
Pre-Owned
$179.90
or Best Offer
+$36.15 delivery
Located in United States
wheezer432 100% positive (1.1K)
Annette Himstedt Doll Club Mini 11in Lalka
Annette Himstedt Doll Club Mini 11in LalkaOpens in a new window or tab
Pre-Owned
$150.00
or Best Offer
+$35.73 delivery
Located in United States
ttwcoll91 100% positive (1K)
OOAK LALKA Bild LILLI SEVERINE SYLVAIN fit DOLL Custom shirtwaist DRESS 💜💙🧡💛
OOAK LALKA Bild LILLI SEVERINE SYLVAIN fit DOLL Custom shirtwaist DRESS 💜💙🧡💛Opens in a new window or tab
Pre-Owned
$40.00
Buy It Now
"""

# ==============================================================================
# 2. REGULAR EXPRESSION EXTRACTION
# ==============================================================================
#Patterns: I extracted Prices in US dollars, seller positive Feedback percentages and counts from within parentheses which is
#assumably rating counts by consumers.
# In the section of prices I was only able to extract prices in US dollars and I could not extract the prices without
#decimal point. When it comes to Pattern 1 and 2, I extracted data effectively. Especially, the 3rd one included the
# data contains "k" which represents thousands

import re

print("--- 2. Regular Expression Extraction ---")

# Pattern 1: Extract prices in US dollars (e.g., $20.00, $402.81)
price_pattern = r'\$\d{1,3}(?:,?\d{3})*\.\d{2}'
prices = re.findall(price_pattern, text)
print(f"Extracted Prices: {prices}")

# Pattern 2: Extract seller positive feedback percentages (e.g., 100%, 98.1%)
rating_pattern = r'\d{1,3}(?:\.\d)?%'
ratings = re.findall(rating_pattern, text)
print(f"Extracted Seller Ratings: {ratings}")

# Pattern 3: Extract counts from within parentheses (e.g., (45), (11.5K))
count_pattern = r'\(([\d\.,Kk]+)\)'
counts = re.findall(count_pattern, text)
print(f"Extracted Counts in Parentheses: {counts}\n")


# ==============================================================================
# 3. NLP PRE-PROCESSING
# ==============================================================================
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from collections import Counter

print("--- 3. NLP Pre-processing ---")

# Download necessary NLTK packages if you haven't already.
# This can be commented out after the first successful run.
#nltk.download('punkt', quiet=True)
#nltk.download('averaged_perceptron_tagger', quiet=True)

# 1. Tokenize and convert to lowercase.
tokens = [word.lower() for word in word_tokenize(text)]

# 2. Remove stop words (with a custom list for this specific text).
stop_words = set(stopwords.words('english'))
custom_stop_words = {'shop', 'ebay', 'offer', 'best', 'buy', 'new', 'brand', 'opens', 'window', 'tab',
                     'shipping', 'delivery', 'located', 'pre-owned', 'read', 'opens', 'customs', 'services',
                     'international', 'tracking', 'provided', 'or', 'match', 'see', 'items', 'find', 'style'}
stop_words.update(custom_stop_words)

# Filter out stop words and non-alphabetic tokens.
filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

# 3. Lemmatization
# Choice Justification: Lemmatization was chosen over stemming because it converts words
# to their meaningful dictionary form, which is better for preserving the semantic value
#  of the keywords in the listings.
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# Count the frequency of the processed tokens.
token_counts = Counter(lemmatized_tokens)

# Display the top 15 most common tokens.
print("Top 15 Processed Tokens:")
print(f"{token_counts.most_common(15)}\n")
#[('lalka', 40), ('doll', 31), ('lilli', 30), ('positive', 22), ('julian', 22), ('rare', 22),
#('kalinowski', 21), ('sylvain', 20), ('ooak', 19), ('severine', 17), ('bild', 16), ('united', 11),
# ('watcher', 11), ('state', 9), ('south', 7)]
# ==============================================================================
# 4. REGEX + NLP COMBINATION
# ==============================================================================
print("--- 4. Regex + NLP Combination ---")

# Tokenize and apply Part-of-Speech (POS) tagging.
tokens_for_pos = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens_for_pos)

number_noun_pairs = []
for i in range(len(pos_tags) - 1):
    # Check if the token is a number (POS tag 'CD' - Cardinal Number).
    if pos_tags[i][1] == 'CD':
        # Check if the following token is a noun (POS tags 'NN' or 'NNS').
        if pos_tags[i+1][1] in ['NN', 'NNS']:
            pair = (pos_tags[i][0], pos_tags[i+1][0])
            number_noun_pairs.append(pair)

print("Extracted (Number, Noun) Pairs:")
print(f"{number_noun_pairs}\n")
#This approach successfully extracted specific numeric-object pairs such as “17 watchers” or “1 bid.” However, since
#the data was not in complete sentence form, some unintended pairs were also extracted — showing the limitations
#of this method.
# ==============================================================================
# 5. VISUALIZATION
# ==============================================================================
import matplotlib.pyplot as plt
import seaborn as sns

print("--- 5. Visualization ---")
print("Displaying bar chart of top 15 tokens...")

# Prepare the data for plotting.
top_tokens = token_counts.most_common(15)
tokens, counts = zip(*top_tokens)

# Create the bar chart.
plt.figure(figsize=(12, 8))
sns.barplot(x=list(counts), y=list(tokens), palette='plasma')
plt.title('Top 15 Most Frequent Tokens from eBay Listings')
plt.xlabel('Frequency')
plt.ylabel('Tokens')
plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()

#This bar chart visualizes the 15 most frequent words in the preprocessed text. The graph clearly shows that the text
#mainly concerns “lalka” and “doll,” with related keywords like “kalinowski,” “severine,” and “ooak” appearing as
#significant proper nouns and distinguishing features.
# ==============================================================================
# 6. REPORT SUMMARY
# ==============================================================================
print("\n--- 6. Report Summary ---")
report = """
Approach:
This analysis focused on irregular text data collected from eBay listings. First, regular expressions were used 
to extract structured information such as prices and seller ratings. Then, an NLP pipeline (tokenization, stopword 
removal, and lemmatization) was applied to identify key terms in the text. The precision was improved by adding 
custom stopwords specific to this dataset.

Challenges:
The main challenge was the unstructured nature of the text, which contained a lot of noise. As a result, 
the standard stopword list was insufficient and required customization to fit the dataset. Also, I should have excluded 
some words on the top 15th list such as possitive and watchers because it is the words always appeared in every 
searching results and I should have to deal with some words represents "countries" which were not important word when 
it was counted as a separate meaning (eg. state, south)

Findings:
The analysis successfully extracted specific business-related data, such as prices and ratings. NLP results revealed 
that the main topic of the listings centered on “Lalka dolls” associated with “Kalinowski’s novel.” This demonstrates 
that, with appropriate preprocessing, valuable insights can be derived even from irregular and noisy data which are 
mixedn information about the novel"Lalka" and doll" lalka".
"""
print(report)
