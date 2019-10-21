with open('encoded_uuid.txt', 'r', encoding='utf8') as uuid_f:
    uuid = uuid_f.read()
    print('.', uuid, '.')

with open('blog.md', 'r') as blog, open('out.md', 'w', encoding='utf8') as out:
    sentences = blog.read().split('.')
    for sentence in sentences:
        gap = len(sentence)//2
        out.write(sentence[:gap] + str(uuid) + sentence[gap:] + '.')
