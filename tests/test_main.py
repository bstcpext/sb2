from main import main


def test_main_prints(capsys):
    main()
    assert capsys.readouterr().out == "Hello from sb2!\n"
