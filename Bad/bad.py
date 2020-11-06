import argparse
import git
import numpy as np
import time
from PIL import Image


def buildParser():
    parser = argparse.ArgumentParser(description='Branch Analysis Diagram')
    parser.add_argument('path', type=str, help='path to directory or file to be analyzed')
    return parser

def build_disimilarity_matrix(repo, branches, heuristic, verbose=False):
    n = len(branches)

    change_types=[
        'A', # added paths 
        # 'D', # deleted paths
        # 'R', # renamed paths
        # 'C', # copied paths
        # 'M', # modified data
        # 'T', # changed types
    ]

    # construct n by n matrix
    accum = np.zeros((n, n))
    for i in range(n):
        if verbose:
            print('col', i, ";", end='', flush=True)

        for j in range(n):
            if verbose:
                print(j, ' ', end='', flush=True)
            
            diff = repo.commit(branches[i]).diff(branches[j])
            diff_vec = np.zeros((len(change_types), 1))

            for k in range(len(change_types)):
                # have to explicitly expand each generator to get it's length
                diff_vec[k] = len(list(diff.iter_change_type(change_types[k])))

            accum[i, j] = heuristic(diff_vec)

        if verbose:
            print()

    return accum
    

def main():
    args = buildParser().parse_args()

    repo = git.Repo(args.path)

    # lol... python magic
    branches = [r.name for remote in repo.remotes for r in repo.remote(remote).refs if not r.name.endswith('HEAD')]

    # TODO add verbose options
    # print('branches to analyze:', branches)

    # generate matrix
    n = len(branches)
    if n < 2:
        print('ERROR: cannot perform analysis on a single branch')
        exit(1)
    
    print('Generating disimilarity matrix for', n, 'branches.')
    start = time.time()
    disi = build_disimilarity_matrix(
        repo=repo,
        branches=branches, 
        heuristic=sum,
        verbose=True
    )

    print('Matrix generation complete in', (time.time()-start)/60, 'minutes')

    img = Image.fromarray(disi)
    img = img.convert('L')
    img.save('test.png')
    img.show()


def doSomething(x): 
    return x + 1