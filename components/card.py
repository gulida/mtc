from ..base.base import Base


class Card(Base):

    def check_card_visibility(self, how, what):
        return self.is_element_present(how, what)


