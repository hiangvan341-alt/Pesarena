from modules.parsec_room.service import validate_parsec_id, validate_parsec_link

def test_parsec_id_valid(): assert validate_parsec_id('Player_01') == 'Player_01'
def test_parsec_id_empty_allowed(): assert validate_parsec_id('') is None
def test_parsec_id_rejects_spaces():
    try: validate_parsec_id('bad id')
    except ValueError: return
    assert False

def test_parsec_link_valid(): assert validate_parsec_link('https://parsec.gg/g/abc/def')
def test_parsec_link_optional(): assert validate_parsec_link('') is None
def test_parsec_link_rejects_fake_domain():
    for link in ('https://parsec.gg.evil.com/g/a/b','https://evilparsec.gg/g/a/b','http://parsec.gg/g/a/b'):
        try: validate_parsec_link(link)
        except ValueError: continue
        assert False, link

def test_no_new_polling_source():
    src=open('modules/parsec_room/routes.py',encoding='utf-8').read()+open('templates/_room_live_content.html',encoding='utf-8').read()
    assert 'setInterval' not in src and 'setTimeout' not in src

def test_rp_files_untouched_by_module():
    src=open('modules/parsec_room/routes.py',encoding='utf-8').read()
    assert 'rp_' not in src.lower() and 'matches' not in src.lower()
