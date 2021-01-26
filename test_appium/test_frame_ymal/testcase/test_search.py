from test_appium.test_frame_searchpage.app import App


def test_search():
    app = App()
    result = app.start().goto_main().goto_market_page().goto_search()
    assert result
