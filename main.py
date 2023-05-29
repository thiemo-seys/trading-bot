import argparse

from config import Config

def main():
    # parser arguments
    args = parser.parse_args()
    # print variables
    config = Config.from_yaml(args.config)
    print(f"{config=}")


# only execute if this file is ran directly
if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser()
    # add arguments to parser
    parser.add_argument("-c", "--config", help="Config file location", default="default.yaml")
    parser.add_argument("-lf", "--logging_file", help="location of the logging file", default="app.log")
    # execute main function declared above
    main()
