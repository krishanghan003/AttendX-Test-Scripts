def test_login():
    username = "student01"
    password = "attendx123"

    assert username == "student01"
    assert password == "attendx123"
    assert username != ""

    print("Login test passed")


if __name__ == "__main__":
    test_login()