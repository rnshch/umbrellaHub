from selenium.webdriver.common.keys import Keys


def test_search_pupies(py):
    py.visit("https://google.com")
    py.get("[name='q']").type('puppies', Keys.ENTER)
    assert py.should().contain_title('puppies')