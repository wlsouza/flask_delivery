
def test_app_is_created(app):
    assert app.name == "flasklivery.app"


def test_config_is_loaded(config):
    assert config["DEBUG"] is False


def test_request_return_404(client):
    assert client.get("/this_url_doesnt_exist").status_code == 404
