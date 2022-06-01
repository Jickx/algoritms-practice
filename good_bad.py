bad = ['a', 'b', 'c']
good = ['good']

def check_text(text):
    words = text.split()
    good_passed = False
    for word in words:
        if word in bad:
            return 'not passed'
        if word in good:
            good_passed = True
    if good_passed:
        return 'passed'
    else:
        return 'not passed'

assert check_text('a b c good') == 'not passed'
assert check_text('a b bad') == 'not passed'
assert check_text('d good') == 'passed'
assert check_text('d bad') == 'not passed'