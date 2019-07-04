#!/usr/bin/env python3
"""{{ cookiecutter.description }}."""
import os
import traceback

import requests


class State:
    """Holds the state of the application throughout an execution."""

    def __init__(self):
        self.ENVIRONMENT = os.environ["ENVIRONMENT"].lower()
        self.VAULT_URL = "https://vault.tools.{}.tax.service.gov.uk".format(
            self.ENVIRONMENT
        )
        self.VAULT_ROLE_ID = os.environ["VAULT_ROLE_ID"]
        self.VAULT_SECRET_ID = os.environ["VAULT_SECRET_ID"]
        self.DEFAULT_WRAP_TTL = str(60 * 60 * 4)

        self.vault_auth_token = None


def lambda_handler(event, context):
    return main(event["user_name"], event["public_key"], event["ttl"])


def main(user_name, public_key, ttl):
    try:
        state = State()

        vault_authenticate(state)
        signed_cert_response = vault_sign_certificate(state, user_name, public_key, ttl)
        wrapped_token = vault_wrap(state, json_blob=signed_cert_response)

        return {"token": wrapped_token}
    except Exception as e:
        return {"error": str(e), "trace": traceback.format_exc()}


def vault_authenticate(state):
    url = state.VAULT_URL + "/v1/auth/approle/login"
    data = {"role_id": state.VAULT_ROLE_ID, "secret_id": state.VAULT_SECRET_ID}

    response = requests.post(url, json=data).json()

    try:
        state.vault_auth_token = response["auth"]["client_token"]
    except KeyError:
        raise Exception(
            "vault authentication failed!  "
            "is the AppRole for this application configured correctly?"
        )


def vault_sign_certificate(state, user_name, public_key, ttl):
    url = (
        state.VAULT_URL
        # TODO Change this to the real ssh backend!
        + "/v1/ssh-platsec-poc/sign/signer-poc"
    )
    data = {"public_key": public_key, "valid_principals": user_name, "ttl": ttl}
    headers = {"X-Vault-Token": state.vault_auth_token}

    response = requests.post(url, json=data, headers=headers).json()

    try:
        return response["data"]
    except KeyError:
        errors = response.get("errors", [])
        raise Exception("Certificate signing failed.  " + "; ".join(errors))


def vault_wrap(state, json_blob):
    url = state.VAULT_URL + "/v1/sys/wrapping/wrap"
    data = json_blob
    headers = {
        "X-Vault-Token": state.vault_auth_token,
        "X-Vault-Wrap-TTL": state.DEFAULT_WRAP_TTL,
    }

    response = requests.post(url, json=data, headers=headers).json()

    try:
        return response["wrap_info"]["token"]
    except KeyError:
        errors = response.get("errors", [])
        raise Exception("Wrapping failed.  " + "; ".join(errors))
