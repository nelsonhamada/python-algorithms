import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("message", 7) == "egassem"
    assert encrypt_message("message", 1) == "m_egasse"
    assert encrypt_message("message", 2) == "egass_em"
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("message", 4) == "ega_ssem"

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(None, 4)

    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message("message", "3")
