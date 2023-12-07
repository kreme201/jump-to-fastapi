from uuid import uuid4

from starlette.types import ASGIApp, Receive, Scope, Send

from app.database.context import set_db_session_context, reset_db_session_context
from app.database.session import session


class SqlAlchemySessionMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        session_id = str(uuid4())
        context = set_db_session_context(session_id)

        try:
            await self.app(scope, receive, send)
        except Exception as e:
            raise e
        finally:
            session.remove()
            reset_db_session_context(context)
