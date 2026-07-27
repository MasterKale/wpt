from dataclasses import dataclass, asdict
from typing import Any, Optional


@dataclass
class SetCredentialPropertiesProps:
    backupEligibility: Optional[bool]
    backupState: Optional[bool]
    signCount: Optional[int]


def set_credential_properties(
    session: Any,
    authenticator_id: str,
    credential_id: str,
    props: SetCredentialPropertiesProps,
):
    return session.transport.send(
        "POST",
        f"/session/{session.session_id}/webauthn/authenticator/{authenticator_id}/credentials/{credential_id}/props",
        asdict(props),
    )

