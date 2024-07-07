import pytest
from parduotuve import Preke, Parduotuve

@pytest.fixture
def parduotuves_valdymas():
    valdymas = Parduotuve()
    valdymas.prideti_preke(Preke('Lempa', 30, 150))
    valdymas.prideti_preke(Preke('Kavos staliukas', 300, 120))
    valdymas.prideti_preke(Preke('Komoda', 700, 20))
    return valdymas

def test_gauti_preke_pagal_index(parduotuves_valdymas):
    rezultatas = parduotuves_valdymas.gauti_preke_pagal_index(0)
    index_rezultatas = parduotuves_valdymas.prekes[0]
    assert index_rezultatas == rezultatas

def test_gauti_preke_pagal_index_2(parduotuves_valdymas):
    rezultatas = parduotuves_valdymas.gauti_preke_pagal_index(2)
    index_rezultatas = parduotuves_valdymas.prekes[2]
    assert index_rezultatas == rezultatas

def test_istrinti_preke(parduotuves_valdymas):
    parduotuves_valdymas.istrinti_preke(0)
    assert 'Lempa' not in [preke.pavadinimas for preke in parduotuves_valdymas.prekes]

def test_istrinti_preke_komoda(parduotuves_valdymas):
    parduotuves_valdymas.istrinti_preke(2)
    assert 'Komoda' not in [preke.pavadinimas for preke in parduotuves_valdymas.prekes]
    
def test_rikiuoti_pagal_savybe(parduotuves_valdymas):
    rezultatas = parduotuves_valdymas.rikiuoti_pagal_savybe('kaina')
    prekiu_sarasas = [preke for preke in rezultatas]
    assert prekiu_sarasas == ['Lempa | 30.0 | 150', 'Kavos staliukas | 300.0 | 120','Komoda | 700.0 | 20']
    assert prekiu_sarasas == rezultatas

def test_rikiuoti_pagal_savybe_kiekis(parduotuves_valdymas):
    rezultatas = parduotuves_valdymas.rikiuoti_pagal_savybe('kiekis')
    prekiu_sarasas = [preke for preke in rezultatas]
    assert prekiu_sarasas == ['Komoda | 700.0 | 20', 'Kavos staliukas | 300.0 | 120', 'Lempa | 30.0 | 150']
    assert prekiu_sarasas == rezultatas

def test_atnaujinti_preke(parduotuves_valdymas):
    rezultatas = parduotuves_valdymas.atnaujinti_preke()
    
