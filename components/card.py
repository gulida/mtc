from ..base.base import Base


class Card(Base):

    def check_card_visibility(self, how, what):
        return self.is_element_present(how, what)

    def get_all_cards_in_container(self, how, what, element):
        if self.is_element_present(how, what):
            return self.browser.find_elements(how, what)
        else:
            print(f'There is no {element} card')

    def get_all_card_titles(self, how, what, element):
        if self.is_element_present(how, what):
            card_titles = []
            found_data = self.browser.find_elements(how, what)
            for e in found_data:
                card_titles.append(e.text)
            return card_titles
        else:
            print(f'There is no {element} card title')