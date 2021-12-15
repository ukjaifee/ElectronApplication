import pytest

from pageObjects.AtomMainPage import AtomMainPage
from utility.BaseClass import BaseClass
from data.AtomData import AtomData


class TestElectronAPIAPP(BaseClass):
    atomAppPage = None

    @pytest.fixture
    def initialize(self) -> list:
        atomAppPage = AtomMainPage(self.driver)
        return [atomAppPage]

    def test_verify_welcome_checkbox(self, initialize):
        initialize[0].home_Component().is_Displayed()
        flag = initialize[0].home_Component().check_welcome_checkbox()
        assert flag is True

    def test_change_theme(self, atom_theme, initialize):
        initialize[0].home_Component().change_atom_theme(atom_theme[1])

    @pytest.fixture(params=AtomData.themes)
    def atom_theme(self, request):
        return request.param
