import random

# First words: Adjectives & descriptors
FIRST_WORDS = [
    "tricky", "sharp", "cool", "swift", "brave", "clever", "silent", "bold",
    "mighty", "wild", "calm", "fierce", "gentle", "happy", "jolly", "keen",
    "lively", "merry", "noble", "proud", "quick", "smart", "witty", "zesty",
    "bright", "cosmic", "daring", "eager", "fancy", "grand", "hyper", "icy",
    "jazzy", "lucky", "magic", "neon", "omega", "prime", "royal", "solar",
    "turbo", "ultra", "vivid", "wise", "young", "zealous", "agile", "breezy",
    "crisp", "dizzy", "epic", "frosty", "golden", "hidden", "iron", "jade",
    "kind", "lunar", "misty", "nimble", "odd", "peppy", "quiet", "rapid",
    "sly", "tough", "urban", "velvet", "warm", "xeno", "yellow", "zen",
    "ancient", "blazing", "chilly", "digital", "electric", "flying", "giant",
    "honest", "infinite", "jumping", "knightly", "loopy", "mystic", "noisy",
    "orbital", "phantom", "quantum", "rebel", "shadow", "thunder", "velvety",
    "wandering", "zany", "atomic", "bronze", "crimson", "emerald", "silver"
]

# Second words: Animals, objects, & themes
SECOND_WORDS = [
    "possum", "bear", "cards", "fox", "wolf", "tiger", "eagle", "hawk",
    "shark", "whale", "panda", "koala", "otter", "badger", "falcon", "raven",
    "owl", "viper", "cobra", "dragon", "phoenix", "griffin", "knight", "ninja",
    "pirate", "wizard", "ranger", "scout", "pilot", "captain", "sailor", "viking",
    "comet", "star", "moon", "planet", "nebula", "galaxy", "orbit", "meteor",
    "bolt", "spark", "flame", "frost", "storm", "cloud", "river", "ocean",
    "mountain", "forest", "canyon", "desert", "island", "glacier", "volcano",
    "hammer", "shield", "sword", "arrow", "dagger", "lance", "crown", "ring",
    "gem", "coin", "dice", "chess", "pixel", "glitch", "byte", "cipher",
    "beacon", "radar", "rocket", "rover", "drone", "mech", "bot", "core",
    "cactus", "acorn", "maple", "cedar", "bamboo", "clover", "fern", "moss",
    "pebble", "boulder", "crystal", "quartz", "onyx", "topaz", "ruby", "pearl",
    "biscuit", "waffle", "noodle", "pickle", "muffin", "taco", "pretzel", "bagel"
]

def generate_username(capitalize=False, min_num=10, max_num=99):
    """Generates a single random username in the format: word1 + word2 + number."""
    word1 = random.choice(FIRST_WORDS)
    word2 = random.choice(SECOND_WORDS)
    number = random.randint(min_num, max_num)

    if capitalize:
        word1 = word1.capitalize()
        word2 = word2.capitalize()

    return f"{word1}{word2}{number}"

def generate_batch(count=10, capitalize=False):
    """Generates a list of unique random usernames."""
    usernames = set()
    while len(usernames) < count:
        usernames.add(generate_username(capitalize=capitalize))
    return list(usernames)

if __name__ == "__main__":
    print("--- Lowercase Examples ---")
    for name in generate_batch(count=5, capitalize=False):
        print(name)

    print("\n--- CamelCase Examples ---")
    for name in generate_batch(count=5, capitalize=True):
        print(name)
