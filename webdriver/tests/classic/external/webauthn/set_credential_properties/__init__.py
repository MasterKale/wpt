from dataclasses import dataclass, asdict
from typing import Any, Optional, Union


@dataclass
class SetCredentialPropertiesProps:
    backupEligibility: Optional[bool]
    backupState: Optional[bool]
    signCount: Optional[int]


def set_credential_properties(
    session: Any,
    authenticator_id: str,
    credential_id: str,
    props: Union[SetCredentialPropertiesProps, dict],
):
    """
    This method calls the Set Credential Properties endpoint as per the WebAuthn spec:

    https://w3c.github.io/webauthn/#sctn-automation-set-credential-properties

    `props` supports an instance of `SetCredentialPropertiesProps`, but also accepts a raw `dict`
    value. The latter allows for quick-and-dirty passing in of partially populated properties:

    ```
    props = SetCredentialPropertiesProps(
        backupEligibility=True,
        backupState=True,
        signCount=0,
    )

    props = asdict(props)
    del props["signCount"]  # Don't send signCount at all

    set_credential_properties(..., props=props)
    ```
    """
    if isinstance(props, SetCredentialPropertiesProps):
        props = asdict(props)

    return session.transport.send(
        "POST",
        f"/session/{session.session_id}/webauthn/authenticator/{authenticator_id}/credentials/{credential_id}/props",
        props,
    )
