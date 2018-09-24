def generate_name_from_sha1(nouns, adjectives, sha1):
    nouns_count = len(nouns)
    adjectives_count = len(adjectives)

    variants_count = nouns_count * adjectives_count

    ref_name = sha1[:8]
    num = int(ref_name, 16)

    num = num % variants_count

    adjective = adjectives[int(num % adjectives_count)]
    noun = nouns[int(num / adjectives_count)]

    return f'{adjective} {noun}'
