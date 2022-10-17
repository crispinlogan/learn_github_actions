import nox


@nox.session(python=["3.10"])
def tests(session):
    # session.install('pytest', 'pytest-cov')
    session.run("poetry", "install", "--only", "dev", external=True)
    session.run("pytest", "--cov")
