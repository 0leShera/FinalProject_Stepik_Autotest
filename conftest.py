import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
	parser.addoption('--language', action='store', default='en', help='Choose language: ru, en, fr...')

@pytest.fixture(scope='function')
def browser(request):
	selection_browser = request.config.getoption('browser_name')
	selection_language = request.config.getoption('language')
	print(f'\nstart {selection_browser} browser for test..\nselect {selection_language} language for test..')

	if selection_browser == "chrome":
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': selection_language})
		browser = webdriver.Chrome(options=options)
	elif selection_browser == "firefox":
		fp = webdriver.FirefoxProfile()
		fp.set_preference('intl.accept_languages', selection_language)
		browser = webdriver.Firefox(firefox_profile=fp)
	else:
		raise pytest.UsageError('--browser_name should be chrome or firefox')

	yield browser
	print('\nquit browser..')
	browser.quit()
