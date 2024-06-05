## Description

The repository contains tests for use with the following command line options:

Agenda:
1. 1_verbose_option use for -v option;
2. 2_collect_only_option for --collect-only option;
3. 3_exitfirst_and_maxfail_options for -x and --maxfail options;
4. 4_capture_and_showlocals_options for -s and --showlocals options;
5. 5_k_expression_option for -k option;
6. 6_mark_option for -m option;
7. 7_quiet_option for -q option. 

Refer to a proper lesson for a examples and commands to play with.

*Regardless of this, you can try running different tests with different options and combine them to get more experience.*

## Installation and execution

First install dependencies:
```sh
pip install -r requirements.txt
```

Run examples with:
```sh
cd <folder>
python -m pytest -<option>
```

## Documentation
On your journey, you can use the [official pytest documentation](https://docs.pytest.org/en/7.2.x/).