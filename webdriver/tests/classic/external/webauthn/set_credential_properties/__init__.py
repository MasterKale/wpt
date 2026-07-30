from dataclasses import dataclass, asdict
from typing import Any, Union

from .. import DataclassOmittableFields


@dataclass
class SetCredentialPropertiesProps(DataclassOmittableFields):
    """
    Set Credential Properties Parameters:

    https://w3c.github.io/webauthn/#set-credential-properties-parameters
    """
    _UNSET = DataclassOmittableFields.UNSET  # Alias the sentinel field type for readability
    backupEligibility: Union[bool, _UNSET] = _UNSET
    backupState: Union[bool, _UNSET] = _UNSET
    signCount: Union[int, None, _UNSET] = _UNSET


def set_credential_properties(
    session: Any,
    authenticator_id: str,
    credential_id: str,
    props: SetCredentialPropertiesProps,
):
    """
    WebAuthn Virtual Authenticator Set Credential Properties endpoint:

    https://w3c.github.io/webauthn/#sctn-automation-set-credential-properties
    """
    props = asdict(props, dict_factory=DataclassOmittableFields.dict_factory)

    return session.transport.send(
        "POST",
        f"/session/{session.session_id}/webauthn/authenticator/{authenticator_id}/credentials/{credential_id}/props",
        props,
    )
