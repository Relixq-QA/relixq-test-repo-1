
# RelixQ QA — Public Repository

This repository contains synthetic security test data
for testing source-control integration and security scanning.

## Test cases

1. RSA-2048 key generation in `crypto_test.py`
2. SHA-1 hashing in `crypto_test.py`
3. Hard-coded placeholder credentials in `config_test.py`

## Expected validation

- Repository can be accessed as a public repository.
- The main and feature/login branches can be selected.
- RelixQ can attempt to scan the committed files.
- Record which cryptographic patterns and secret-like values
  the scanner detects.

## Safety

All credentials are fake test values.
No real credentials or private keys are stored here.
