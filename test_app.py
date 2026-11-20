from app import app


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == (
        "Hello, DevOps World! We are LIVE on Render!"
    )

