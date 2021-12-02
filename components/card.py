import time

from ..base.base import Base


# How it works:
# card_collection = self.get_base_card_collection_with_title_edit_delete()
# card_title - string
def press_card_edit_button(card_collection, card_title):
    message_flag = True
    if len(card_collection):
        for item in card_collection.values():
            if item['title'] == card_title:
                item['edit'].click()
                message_flag = False
                break
        if message_flag:
            print(f'Could not find card with {card_title} title!')
    else:
        print('There is no card to edit!')


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

    def get_base_card_collection_with_title_edit_delete(self, how_card, what_card,
                                                        how_title, what_title,
                                                        how_edit, what_edit,
                                                        how_delete, what_delete,
                                                        card_name):
        collection = {}
        if self.is_element_present(how_card, what_card):
            cards = self.browser.find_elements(how_card, what_card)
            titles = self.browser.find_elements(how_title, what_title)
            edit_btns = self.browser.find_elements(how_edit, what_edit)
            delete_btns = self.browser.find_elements(how_delete, what_delete)
            for i in range(len(cards)):
                collection.update({i: {'title': titles[i].text,
                                       'edit': edit_btns[i],
                                       'delete': delete_btns[i]}})
            return collection
        else:
            print(f'{card_name} - does not exist!')

    # How it works:
    # card_collection = self.get_base_card_collection_with_title_edit_delete()
    # card_title - string
    def delete_card(self, card_collection, card_title, how_accept_btn, what_cancel_btn):
        message_flag = True
        if len(card_collection):
            for item in card_collection.values():
                if item['title'] == card_title:
                    item['delete'].click()
                    time.sleep(3)
                    button = self.browser.find_element(how_accept_btn, what_cancel_btn)
                    time.sleep(2)
                    button.click()
                    time.sleep(3)
                    message_flag = False
                    break
            if message_flag:
                print(f'Could not find card with {card_title} title!')
        else:
            print('There is no card to delete!')
        time.sleep(3)
