from entities.monster import Monster
from unittest.mock import patch


def test_save():

    monster = Monster("Vampiro", "Ser aesthetic")

    with patch("entities.monster.get_connection") as mock_connection:

        monster.save()

        # confirmado del guardado
        mock_connection.return_value.commit.assert_called_once()

        #assert False 