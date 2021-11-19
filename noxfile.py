from os import getenv

from nox import session, parametrize, options

options.sessions = ["docs(html)"]


@session(venv_backend="conda", reuse_venv=True, python="3.9")
@parametrize("pdf", [False, True], ids=["html", "pdf"])
def docs(session, pdf):
    "build the `pidgy` documentation with `jupyter-book`"
    args = ()
    if pdf:
        args += "--builder", "pdflatex"
        session.conda_install("-c", "conda-forge", "tectonic")
    session.install("jupyter-book", "jupyterbook-latex",
                    "sphinx-autoapi")

    session.run("jb", "build", ".", *session.posargs, *args)
