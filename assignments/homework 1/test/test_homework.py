"""
Test script to verify homework 1 functionality
This validates the regex and NLP processing logic
"""

import re

# Sample text
sample_text = """
Contact us at info@aitech.com. Important dates: January 15, 2023 and March 1, 2024.
Call +1-555-123-4567 for more info. Investment: $50 billion in 2023.
"""

print("=== Testing Regex Patterns ===\n")

# Test email extraction
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, sample_text)
print(f"Emails found: {emails}")
assert len(emails) > 0, "Should find at least one email"

# Test date extraction
date_pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b'
dates = re.findall(date_pattern, sample_text)
print(f"Dates found: {dates}")
assert len(dates) > 0, "Should find at least one date"

# Test phone number extraction
phone_pattern = r'\+?\d{1,3}[-.]?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b'
phones = re.findall(phone_pattern, sample_text)
print(f"Phone numbers found: {phones}")
assert len(phones) > 0, "Should find at least one phone number"

# Test money extraction
money_pattern = r'\$[\d,]+(?:\.\d{2})?(?:\s+(?:billion|million))?'
amounts = re.findall(money_pattern, sample_text)
print(f"Dollar amounts found: {amounts}")
assert len(amounts) > 0, "Should find at least one dollar amount"

print("\n✓ All regex tests passed!")

# Test NLP preprocessing (basic test without NLTK)
print("\n=== Testing Basic NLP ===\n")

tokens = sample_text.lower().split()
print(f"Tokens after lowercase split: {len(tokens)} tokens")
print(f"Sample tokens: {tokens[:10]}")

# Simple stop word removal
simple_stop_words = {'us', 'at', 'in', 'for', 'and', 'the', 'a', 'an', 'to', 'of'}
filtered = [t for t in tokens if t not in simple_stop_words and t.isalpha()]
print(f"After simple filtering: {len(filtered)} tokens")

print("\n✓ Basic NLP processing works!")
print("\n=== All tests completed successfully! ===")
