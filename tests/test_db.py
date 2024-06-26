from sqlalchemy import select

from fast_api_zero.models import User


def test_create_user(session):
    user = User(
        username='leandro', email='leandro@leandro.com', password='senha'
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    result = session.scalar(
        select(User).where(User.email == 'leandro@leandro.com')
    )

    assert result.username == 'leandro'
