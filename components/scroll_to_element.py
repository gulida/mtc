from ..base.base import Base


class ScrollToElement(Base):

    def scroll_to_component(self, how, what):
        element = self.browser.find_element(how, what)
        coordinates = element.location_once_scrolled_into_view  # returns dict of X, Y coordinates
        self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))