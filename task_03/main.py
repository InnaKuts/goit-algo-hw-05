import os.path
from timeit import timeit
from typing import Callable

from kmp_search import kmp_search
from boyer_moore_search import boyer_moore_search
from rabin_karp_search import rabin_karp_search


def measure(
    dataset: dict[str, (str, str)],
    algos: dict[str, Callable[[str, str], int]],
    number=1000,
    skip_runs: list[tuple[str, str]] = None
):
    if skip_runs is None:
        skip_runs = []
    results = {}
    print('>> start measure')
    for (ds_label, ds) in dataset.items():
        ds_results = {}
        results[ds_label] = ds_results
        print(f'\t>> start dataset `{ds_label}`')
        for (algo_label, algo) in algos.items():
            if (ds_label, algo_label) in skip_runs:
                print(f'\t\t== skip algo `{algo_label}`')
                continue
            print(f'\t\t>> start algo `{algo_label}`')
            ds_results[algo_label] = timeit(
                stmt='algo(ds[0], ds[1])',
                globals={'ds': ds, 'algo': algo},
                number=number
            )
            print(f'\t\t<< end algo [result={algo(ds[0], ds[1])}] `{algo_label}`: {ds_results[algo_label]}')
        print(f'\t<< end dataset `{ds_label}`')
    print('<< end measure')
    return results


def read(path: str):
    with open(path, "r") as f:
        return f.read()


def main():
    data1 = read(os.path.join('data', 'data1.txt'))
    data2 = read(os.path.join('data', 'data2.txt'))
    results = measure(
        dataset={
            'data1-existing': (data1, 'від двійкового пошуку відрізняється рухом виключно вперед'),
            'data1-non-existing': (data1, 'від двійкового пошуку non-existing відрізняється рухом виключно вперед'),
            'data2-existing': (data2, 'пливає на швидкість роботи і на об’єм використаної пам’яті. Зме'),
            'data2-non-existing': (data2, 'пливає на швидкість роботи і на об’єм використаної пам’яті. Зме non-existing'),
        },
        algos={
            'kmp_search': kmp_search,
            'boyer_moore_search': boyer_moore_search,
            'rabin_karp_search': rabin_karp_search,
        },
    )
    print(results)


if __name__ == '__main__':
    main()
