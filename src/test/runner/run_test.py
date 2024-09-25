from src.test.runner import Runner

class run_test:

    if __name__ == "__main__":
        runner = Runner()  # Create an instance of the Runner class
        exit_code = runner.run()  # Run the tests
        if exit_code != 0:
            print("Tests failed!")
        else:
            print("All tests passed!")
