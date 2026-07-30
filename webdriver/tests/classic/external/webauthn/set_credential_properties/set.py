from typing import Any

from . import set_credential_properties, SetCredentialPropertiesProps, asdict
from .. import create_credential


def test_set_credential_properties(session: Any, authenticator: str):
    credential_id = "Y3JlZC0w"

    # Add a new credential
    new_credential = create_credential(
        credential_id=credential_id,
        sign_count=1,
    )
    session.web_authn.add_credential(authenticator, new_credential)

    [new_credential] = session.web_authn.get_credentials(authenticator)

    # Establish a baseline of assertions so we know what values we're updating
    assert new_credential["credentialId"] == credential_id
    assert new_credential["backupEligibility"] == False
    assert new_credential["backupState"] == False
    assert new_credential["signCount"] == 1

    # Update the credential
    _props = SetCredentialPropertiesProps(
        backupEligibility=True,
        backupState=True,
        signCount=42,
    )
    set_credential_properties(session, authenticator, credential_id, _props)

    # Assert changes were made to the existing credential
    [updated_credential] = session.web_authn.get_credentials(authenticator)

    assert updated_credential["credentialId"] == credential_id
    assert updated_credential["backupEligibility"] == True
    assert updated_credential["backupState"] == True
    assert updated_credential["signCount"] == 42

def test_set_credential_properties_omit_sign_count(session: Any, authenticator: str):
    credential_id = "Y3JlZDI"

    # Add a new credential
    new_credential = create_credential(credential_id=credential_id, sign_count=1)
    session.web_authn.add_credential(authenticator, new_credential)

    [new_credential] = session.web_authn.get_credentials(authenticator)

    # Establish a baseline of assertions so we know what values we're updating
    assert new_credential["signCount"] == 1

    # Update the credential, omitting `signCount`
    _props = SetCredentialPropertiesProps(
        backupEligibility=True,
        backupState=True,
    )

    set_credential_properties(session, authenticator, credential_id, _props)

    # Assert the existing credential's `signCount` is unchanged
    [updated_credential] = session.web_authn.get_credentials(authenticator)

    assert updated_credential["signCount"] == 1
