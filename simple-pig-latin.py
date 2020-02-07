def pig_it(text):
    import re
    old_parts = re.findall(r'\w+|\W+', text)
    new_parts = []
    for old_part in old_parts:
        if re.search(r'\w+', old_part):
            new_part = old_part[1:] + old_part[0] + 'ay'
        else:
            new_part = old_part
        new_parts.append(new_part)
    return ''.join(new_parts)
