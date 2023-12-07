from contextvars import ContextVar, Token

db_session_context: ContextVar[str] = ContextVar("db_session_context")


def get_db_session_context() -> str:
    return db_session_context.get()


def set_db_session_context(session_id: str) -> Token:
    return db_session_context.set(session_id)


def reset_db_session_context(context: Token) -> None:
    db_session_context.reset(context)
