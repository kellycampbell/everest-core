#!/bin/sh

cd tests
pytest --everest-prefix ../dist core_tests/everestpy.py
