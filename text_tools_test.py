from text_tools import *

assert is_new_entry('------------')
assert not is_new_entry('----------..')
assert not is_new_entry('')

assert is_double_backslash('\\\\')
assert not is_double_backslash('---')

assert is_arxiv_id('arXiv:1612.05693')
assert not is_arxiv_id('Date: Sat, 17 Dec 2016 01:54:23 GMT   (381kb,D)')

assert not is_date('arXiv:1612.05693')
assert is_date('Date: Sat, 17 Dec 2016 01:54:23 GMT   (381kb,D)')

assert not is_empty('arXiv:1612.05693')
assert is_empty('')

assert not is_categories('arXiv:1612.05693')
assert is_categories('Categories: cs.AI cs.MA cs.RO')

assert get_arxiv_id('arXiv:1612.05693') == '1612.05693'

assert get_date('Date: Sat, 17 Dec 2016 01:54:23 GMT   (381kb,D)') == datetime(2016, 12, 17, 1, 54, 23)

assert get_authors('Authors: Hang Ma, Sven Koenig') == 'Hang Ma, Sven Koenig'

assert get_categories('Categories: cs.AI cs.MA cs.RO') == 'cs.AI cs.MA cs.RO'

assert parse_date('Sat, 17 Dec 2016 07:03:38 GMT') == datetime(2016, 12, 17, 7, 3, 38)

assert is_title('Title: Control of a Bucket-Wheel f')
assert get_title('Title: Control of a Bucket-Wheel f') == 'Control of a Bucket-Wheel f'

assert is_section('Journal-ref: In Pr')
assert not is_section('Journal ref: In Pr')