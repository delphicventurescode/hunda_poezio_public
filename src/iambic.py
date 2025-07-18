import nltk
import random

# Download CMU dictionary if not already done
nltk.download('cmudict')

# Load CMU Pronouncing Dictionary
cmu = nltk.corpus.cmudict.dict()

def is_iambic(pron):
    """Check if a pronunciation is iambic pentameter: 10 syllables alternating unstressed-stressed."""
    stress_pattern = [s[-1] for s in pron if s[-1].isdigit()]
    if len(stress_pattern) != 10:
        return False
    return all((i % 2 == 0 and stress == '0') or (i % 2 == 1 and stress == '1')
               for i, stress in enumerate(stress_pattern))

def get_iambic_words():
    """Get words that could fit into an iambic meter."""
    iambic_words = []
    for word, prons in cmu.items():
        for pron in prons:
            if len([s for s in pron if s[-1].isdigit()]) == 2:  # two-syllable word
                stress = [s[-1] for s in pron if s[-1].isdigit()]
                if stress == ['0', '1']:  # iambic foot
                    iambic_words.append(word)
    return list(set(iambic_words))

iambic_pairs = get_iambic_words()

def generate_line():
    """Generate a 10-syllable iambic pentameter line."""
    line = []
    syllables = 0
    while syllables < 10:
        candidates = [w for w in iambic_pairs if syllables + 2 <= 10]
        if not candidates:
            break
        word = random.choice(candidates)
        line.append(word)
        syllables += 2
    return ' '.join(line).capitalize() + '.'

# Generate a dog-themed line
for i in range(5):
    print(generate_line())
