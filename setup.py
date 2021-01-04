from setuptools import setup, find_packages

requirements = [
    "fastapi==0.63.0",
    "pydantic==1.7.3",
    "starlette==0.13.6",
    "uvicorn==0.13.3",
    "requests-2.25.1",
]

test_requirements = [
    "pytest==6.0.1",
    "pytest-cov==2.10.1",
    "pylint==2.5.3",
    "pytype==2020.12.23",
    "flake8==3.8.3",
    "black==19.10b0",
]

setup(
    name="4tfPlaylistAnalysis",
    version="0.1",
    description="analyze spotify playlists",
    url="",
    author="Michael Tanner",
    author_email="tanner.mbt@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    tests_require=requirements + test_requirements,
    extras_require={"test": requirements + test_requirements},
    python_requires="~=3.7",
    entry_points={"console_scripts": ["run_svc=src.app.service:start_serving"]},
)
