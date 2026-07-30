from dataclasses import dataclass, asdict
from typing import Any, Optional, Union, Literal




@dataclass
class SetCredentialPropertiesProps:
    """
    This dataclass allows for partial initialization of values. Values not explicitly specified
    can be omitted by passing `SetCredentialPropertiesProps.dict_factory` in as the `dict_factory`
    kwarg when passing an instance of this dataclass into `dataclasses.asdict`:

    Example:
    ```
    props = SetCredentialPropertiesProps(backupEligibility=True)

    props_dict = asdict(props, dict_factory=SetCredentialPropertiesProps.dict_factory)
    print(props_dict)  # {'backupEligibility': True}
    ```
    """
    _UNSET = Literal["UNSET"]

    backupEligibility: Union[bool, _UNSET] = _UNSET
    backupState: Union[bool, _UNSET] = _UNSET
    signCount: Union[int, None, _UNSET] = _UNSET

    @staticmethod
    def dict_factory(items):
        return { k: v for (k, v) in items if v is not SetCredentialPropertiesProps._UNSET }


def set_credential_properties(
    session: Any,
    authenticator_id: str,
    credential_id: str,
    props: SetCredentialPropertiesProps,
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
    props = asdict(props, dict_factory=SetCredentialPropertiesProps.dict_factory)

    return session.transport.send(
        "POST",
        f"/session/{session.session_id}/webauthn/authenticator/{authenticator_id}/credentials/{credential_id}/props",
        props,
    )
