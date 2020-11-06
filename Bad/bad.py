import argparse
import git


def buildParser():
    parser = argparse.ArgumentParser(description='Branch Analysis Diagram')
    parser.add_argument('path', type=str, help='path to directory or file to be analyzed')
    return parser

def main():
    args = buildParser().parse_args()

    repo = git.Repo(args.path)
    print(repo.heads)

def doSomething(x): 
    return x + 1