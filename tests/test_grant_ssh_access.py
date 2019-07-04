"""Test the main module."""
import json
import re

import pytest
import responses
from grant_ssh_access import grant_ssh_access


@pytest.fixture(autouse=True)
def default_environment(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "integration")
    monkeypatch.setenv("VAULT_ROLE_ID", "vault_role_id")
    monkeypatch.setenv("VAULT_SECRET_ID", "vault_secret_id")


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps


def test_happy_path(mocked_responses):
    mocked_responses.add(
        mocked_responses.POST,
        url=re.compile(r".*/v1/auth/approle/login"),
        body=json.dumps({"auth": {"client_token": "vault-auth-token"}}),
    )

    mocked_responses.add(
        mocked_responses.POST,
        url=re.compile(r".*/v1/ssh-platsec-poc/sign/signer-poc"),
        body=json.dumps({"data": {"some": "data"}}),
    )

    mocked_responses.add(
        mocked_responses.POST,
        url=re.compile(r".*/v1/sys/wrapping/wrap"),
        body=json.dumps({"wrap_info": {"token": "token"}}),
    )

    response = grant_ssh_access.main("", "", "")
    assert "token" in response


def test_bad_auth_response(mocked_responses):
    mocked_responses.add(
        mocked_responses.POST,
        url=re.compile(r".*/v1/auth/approle/login"),
        body=json.dumps({"bad": {}}),
    )

    response = grant_ssh_access.main("", "", "")
    assert "error" in response


def test_bad_sign_certificate_response(mocked_responses):
    mocked_responses.add(
        mocked_responses.POST,
        url=re.compile(r".*/v1/auth/approle/login"),
        body=json.dumps({"auth": {"client_token": "vault-auth-token"}}),
    )

    mocked_responses.add(
        mocked_responses.POST,
        url=re.compile(r".*/v1/ssh-platsec-poc/sign/signer-poc"),
        body=json.dumps({"bad": {}}),
    )

    response = grant_ssh_access.main("", "", "")
    assert "error" in response


def test_bad_wrapping_response(mocked_responses):
    mocked_responses.add(
        mocked_responses.POST,
        url=re.compile(r".*/v1/auth/approle/login"),
        body=json.dumps({"auth": {"client_token": "vault-auth-token"}}),
    )

    mocked_responses.add(
        mocked_responses.POST,
        url=re.compile(r".*/v1/ssh-platsec-poc/sign/signer-poc"),
        body=json.dumps({"data": {"some": "data"}}),
    )

    mocked_responses.add(
        mocked_responses.POST,
        url=re.compile(r".*/v1/sys/wrapping/wrap"),
        body=json.dumps({"bad": {}}),
    )

    response = grant_ssh_access.main("", "", "")
    assert "error" in response
